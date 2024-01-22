def app_intro():
  return """
  <div style='text-align: left; padding: 20px; border-radius: 10px;'>
  <h1 style='text-align: center; color: #333;'>NaturalViz : Data Exploration and Visualization with NLP </h1>
  

  <p style='font-size: 18px; color: #444;'>Welcome to NaturalViz!  This app explores how Language Models (LLMs) can help you visualize data  just by talking to it!. we originaly wrote NaturalViz to use OpenAI functions but now have been fully converted to use  Mistral-8x7B-Instruct </p>

  <h3 style='color: #737373;'>Key Features: </h3>
  <ul>
    <li>Turn natural language  into Python code  for visualizations! ✨</li>
    <li>Chat with a friendly bot  to discover insights in your data. </li>
    <li>Made with Langchain 0.1.0. </li>
  </ul>

  <h3 style='color: #737373;'>Under the Hood: ⚙️</h3>
  <p style='font-size: 16px;'>This app uses the  <a href="https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1">Mistral-8x7B-Instruct-v0.1 LLM</a> to understand your questions and create visualizations. </p>

  <h3 style='color: #737373;'>Get Started: </h3>
  <p style='font-size: 16px;'>Ask your data questions in plain language and let the magic happen! 🪄 The bot is here to help if you need it. Dataset used: <a href="https://www.kaggle.com/datasets/crawford/80-cereals">80 Cereals</a> </p>
  </div>
  """


def how_use_intro():
    return """
    <div style='text-align: left; padding: 20px; border-radius: 10px;'>
    <h2 style='text-align: center; color: #333;'>Unlock Insights with NaturalViz! 🌐🔍</h2>
    <br>
    <h3 style='color: #777;'>How to Use:</h3>
    <ul style='font-size: 16px; color: #555;'>
    <li><b>NLP-Driven Visualization:</b> Head to the first tab to explore NLP-driven data visualizations. Enter your queries in natural language, click "Submit," and witness dynamic and personalized visual insights generated by the power of Language Models.</li>
    <li><b>Data Exploration Chatbot:</b> In the second tab, engage with our chatbot. Ask questions about the dataset, request specific visualizations, and let the chatbot guide you through the exploration process using the latest advancements in natural language understanding.</li>
    <li><b>Code and Analysis:</b> Delve into the generated code and analysis in the dedicated code section for the NLP-driven visualization. Gain insights into the methodology and technical prowess behind the visualizations, showcasing the experimental nature of our approach.</li>
    </ul>
    <br>
    </div>
"""
