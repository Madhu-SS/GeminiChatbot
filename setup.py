from setuptools import find_packages,setup

setup(
    name='chatbot',
    version='0.0.1',
    author='madhu s s',
    author_email='madhugowda426@gmail.com',
    install_requires=['python-magic-bin==0.4.14','libmagic','unstructured','google-generativeai','langchain','python-dotenv','streamlit','langchain-google-genai','faiss_cpu'],
    packages=find_packages()
)