uploaded_file = st.file_uploaded(
  "Upload your Resume",
  type=["pdf"]
)
if uploaded_file is not None:
      reader = PdfReader(uploaded_file)
  text = ""
for range in reader.pages:
  text += page.extract_text()
  
