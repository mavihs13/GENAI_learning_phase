
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    PydanticOutputParser
)
from langchain_core.runnables import RunnableBranch, RunnableLambda

from pydantic import BaseModel, Field
from typing import Literal


# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Feedback Manager",
    page_icon="📋",
    layout="wide"
)

load_dotenv()


# -------------------- CUSTOM CSS --------------------

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    .main-title {
        font-size: 32px;
        font-weight: 700;
        color: #172033;
        margin-bottom: 4px;
    }

    .sub-title {
        color: #64748b;
        font-size: 15px;
        margin-bottom: 28px;
    }

    .section-title {
        font-size: 19px;
        font-weight: 650;
        color: #172033;
        margin-bottom: 12px;
    }

    .result-card {
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        background: #ffffff;
        margin-top: 12px;
    }

    .positive {
        color: #15803d;
        font-size: 23px;
        font-weight: 700;
    }

    .negative {
        color: #dc2626;
        font-size: 23px;
        font-weight: 700;
    }

    .muted {
        color: #64748b;
        font-size: 13px;
    }

    div.stButton > button {
        border-radius: 8px;
        font-weight: 600;
        min-height: 42px;
    }

    [data-testid="stSidebar"] {
        border-right: 1px solid #e2e8f0;
    }

</style>
""", unsafe_allow_html=True)


# -------------------- LANGCHAIN SETUP --------------------

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="The sentiment of the feedback"
    )


@st.cache_resource
def load_chain():

    parser1 = StrOutputParser()

    parser2 = PydanticOutputParser(
        pydantic_object=Feedback
    )

    model = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.2
    )

    prompt1 = PromptTemplate(
        template="""
        Classify the sentiment of the following feedback
        as positive or negative.

        Feedback: {feedback}

        {format_instructions}
        """,
        input_variables=["feedback"],
        partial_variables={
            "format_instructions": parser2.get_format_instructions()
        }
    )

    prompt2 = PromptTemplate(
        template="""
        Write a polite and appreciative response to this
        positive customer feedback.

        Feedback: {feedback}
        """,
        input_variables=["feedback"]
    )

    prompt3 = PromptTemplate(
        template="""
        Write a professional and empathetic response to this
        negative customer feedback. Acknowledge the issue
        and offer help.

        Feedback: {feedback}
        """,
        input_variables=["feedback"]
    )

    classify_chain = prompt1 | model | parser2

    # Preserve the original feedback for the response prompt.
    positive_chain = (
        RunnableLambda(lambda x: x["feedback"])
        | prompt2
        | model
        | parser1
    )

    negative_chain = (
        RunnableLambda(lambda x: x["feedback"])
        | prompt3
        | model
        | parser1
    )

    branch_chain = RunnableBranch(
        (
            lambda x: x["sentiment"].sentiment == "positive",
            positive_chain
        ),
        (
            lambda x: x["sentiment"].sentiment == "negative",
            negative_chain
        ),
        RunnableLambda(lambda x: "No valid sentiment detected")
    )

    # Keep the original feedback and classification together.
    from langchain_core.runnables import RunnablePassthrough

    chain = (
        RunnablePassthrough.assign(sentiment=classify_chain)
        | branch_chain
    )

    return chain


# -------------------- SESSION STATE --------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

if "sentiment" not in st.session_state:
    st.session_state.sentiment = None


# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown("## 📋 Feedback Manager")

    st.caption("Customer experience workspace")

    st.divider()

    st.markdown("### Navigation")
    st.markdown("📊  Feedback Analysis")
    st.markdown("🕘  Analysis History")

    st.divider()

    st.markdown("### About")
    st.caption(
        "Analyze customer feedback, identify sentiment, "
        "and generate suitable business responses."
    )

    st.divider()

    st.caption("Powered by LangChain + Groq")


# -------------------- MAIN HEADER --------------------

st.markdown(
    '<div class="main-title">Customer Feedback Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Understand customer sentiment and prepare appropriate responses.'
    '</div>',
    unsafe_allow_html=True
)


# -------------------- METRICS --------------------

total = len(st.session_state.history)

positive_count = sum(
    1 for item in st.session_state.history
    if item["sentiment"] == "positive"
)

negative_count = total - positive_count

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Analyses", total)

with col2:
    st.metric("Positive Feedback", positive_count)

with col3:
    st.metric("Negative Feedback", negative_count)


st.divider()


# -------------------- FEEDBACK INPUT --------------------

left, right = st.columns([1.05, 0.95], gap="large")

with left:

    st.markdown(
        '<div class="section-title">Enter Customer Feedback</div>',
        unsafe_allow_html=True
    )

    feedback_text = st.text_area(
        "Customer feedback",
        placeholder="Example: The product quality is excellent and delivery was very fast. I am really happy with the service.",
        height=220,
        label_visibility="collapsed",
        key="feedback_input"
    )

    st.caption(f"{len(feedback_text)} characters")

    analyze = st.button(
        "Analyze Feedback",
        type="primary",
        use_container_width=True
    )

    if analyze:

        if not feedback_text.strip():
            st.warning("Please enter customer feedback first.")

        else:
            try:
                with st.spinner("Analyzing customer feedback..."):

                    chain = load_chain()

                    result = chain.invoke({
                        "feedback": feedback_text
                    })

                    # Get the classification separately.
                    # This uses the same model workflow.
                    sentiment = chain.steps[0].invoke({
                        "feedback": feedback_text
                    })["sentiment"].sentiment

                    st.session_state.result = result
                    st.session_state.sentiment = sentiment

                    st.session_state.history.insert(0, {
                        "feedback": feedback_text,
                        "sentiment": sentiment,
                        "response": result
                    })

            except Exception as e:
                st.error(f"Something went wrong: {e}")


# -------------------- RESULT PANEL --------------------

with right:

    st.markdown(
        '<div class="section-title">Analysis Result</div>',
        unsafe_allow_html=True
    )

    if st.session_state.result:

        sentiment = st.session_state.sentiment

        if sentiment == "positive":

            st.success("Positive sentiment detected")

            st.markdown(
                '<div class="positive">Positive Feedback</div>',
                unsafe_allow_html=True
            )

            st.caption(
                "The customer has expressed satisfaction."
            )

        else:

            st.error("Negative sentiment detected")

            st.markdown(
                '<div class="negative">Negative Feedback</div>',
                unsafe_allow_html=True
            )

            st.caption(
                "The customer has expressed dissatisfaction."
            )

        st.markdown("#### Suggested Business Response")

        st.text_area(
            "Generated response",
            value=st.session_state.result,
            height=180,
            key="response_display"
        )

        st.button(
            "Copy response",
            use_container_width=True,
            on_click=lambda: st.session_state.update(
                copied_response=st.session_state.result
            )
        )

        if st.session_state.get("copied_response"):
            st.code(st.session_state.copied_response)

    else:

        st.info(
            "Your sentiment analysis and suggested response "
            "will appear here after you submit feedback."
        )

        st.markdown("""
        **What you will get:**

        - Customer sentiment classification
        - Positive or negative status
        - Professionally written response
        """)


# -------------------- HISTORY --------------------

st.divider()

st.markdown(
    '<div class="section-title">Recent Analysis History</div>',
    unsafe_allow_html=True
)

if st.session_state.history:

    for index, item in enumerate(
        st.session_state.history[:5]
    ):

        with st.expander(
            f"{item['sentiment'].upper()} — {item['feedback'][:65]}"
        ):

            st.write("**Customer Feedback:**")
            st.write(item["feedback"])

            st.write("**Suggested Response:**")
            st.write(item["response"])

else:
    st.caption("No feedback has been analyzed yet.")
