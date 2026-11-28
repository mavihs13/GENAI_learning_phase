
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv

load_dotenv()

# -------------------------------
# 1. Streamlit Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Notes & Quiz Generator",
    page_icon="📚",
    layout="wide"
)

# -------------------------------
# 2. Initialize LLM Models
# -------------------------------

@st.cache_resource
def load_models():

    model1 = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.3
    )

    model2 = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.5
    )

    return model1, model2


model1, model2 = load_models()

parser = StrOutputParser()

# -------------------------------
# 3. Define Prompts
# -------------------------------

prompt1 = PromptTemplate(
    template="""
    Generate clear, short and well-structured study notes
    on the following topic:

    {topic}
    """,
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="""
    Generate 5 simple quiz questions with answers
    based on the following notes:

    {notes}

    Include multiple-choice options and mark the correct answer.
    """,
    input_variables=["notes"]
)

prompt3 = PromptTemplate(
    template="""
    Combine the following notes and quiz into one
    well-structured document.

    NOTES:
    {notes}

    QUIZ:
    {quize}
    """,
    input_variables=["notes", "quize"]
)

# -------------------------------
# 4. Create LangChain Workflow
# -------------------------------

notes_chain = prompt1 | model1 | parser

quiz_chain = prompt2 | model2 | parser

# Generate notes once and then generate quiz
parallel_chain = (
    RunnablePassthrough.assign(
        notes=notes_chain
    )
    |
    RunnablePassthrough.assign(
        quize=quiz_chain
    )
)

merge_chain = prompt3 | model1 | parser

# -------------------------------
# 5. Streamlit UI
# -------------------------------

st.title("📚 AI Notes & Quiz Generator")

st.caption(
    "Generate study notes, create quizzes and prepare "
    "your revision document using AI."
)

st.divider()

# Topic input
st.subheader("Enter Your Learning Topic")

topic = st.text_input(
    "Topic",
    placeholder="e.g. Cricket, Machine Learning, Computer Networks"
)

# Generate button
if st.button("✨ Generate Notes & Quiz", type="primary"):

    if not topic.strip():

        st.warning("Please enter a valid topic.")

    else:

        try:
            with st.spinner("AI is generating your notes and quiz..."):

                # Step 1: Generate notes and quiz
                result = parallel_chain.invoke({
                    "topic": topic
                })

                # Step 2: Merge both outputs
                final_result = merge_chain.invoke(result)

                # Store results in session state
                st.session_state["notes"] = result["notes"]
                st.session_state["quiz"] = result["quize"]
                st.session_state["final"] = final_result
                st.session_state["topic"] = topic

            st.success("Your study document is ready!")

        except Exception as e:

            st.error("Something went wrong while generating content.")
            st.exception(e)

# -------------------------------
# 6. Display Generated Results
# -------------------------------

if "notes" in st.session_state:

    st.divider()

    st.subheader(
        f"📖 Study Material: {st.session_state['topic']}"
    )

    tab1, tab2, tab3 = st.tabs([
        "📝 Notes",
        "❓ Quiz",
        "📄 Final Document"
    ])

    with tab1:

        st.markdown("### Generated Study Notes")

        st.markdown(st.session_state["notes"])

        st.download_button(
            label="⬇️ Download Notes",
            data=st.session_state["notes"],
            file_name="study_notes.txt",
            mime="text/plain"
        )

    with tab2:

        st.markdown("### Generated Quiz")

        st.markdown(st.session_state["quiz"])

        st.download_button(
            label="⬇️ Download Quiz",
            data=st.session_state["quiz"],
            file_name="study_quiz.txt",
            mime="text/plain"
        )

    with tab3:

        st.markdown("### Complete Study Document")

        st.markdown(st.session_state["final"])

        st.download_button(
            label="⬇️ Download Complete Document",
            data=st.session_state["final"],
            file_name="study_document.md",
            mime="text/markdown"
        )

    st.divider()

    if st.button("🔄 Generate New Topic"):
        for key in ["notes", "quiz", "final", "topic"]:
            st.session_state.pop(key, None)

        st.rerun()
