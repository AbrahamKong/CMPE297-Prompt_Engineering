# Import necessary libraries
import streamlit as st
import openai

# Configure OpenAI API key
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY


def main():
    st.title("World Class Prompt Beautifier")

    desired_prompt = st.text_area("Enter your desired prompt:")

    # Only display additional fields once a prompt is entered
    if desired_prompt:
        tone = st.selectbox("Select the desired tone (e.g., 'Friendly'):", [
                            "Friendly", "Conversational", "Happy", "Formal", "Instructional", "Professional", "Sarcastic", "Inquisitive", "Inspiring"])
        target_market = st.text_input(
            "Enter the target market (if any, e.g., 'Millennials'):")
        niche = st.text_input(
            "Specify the niche (if any, e.g., 'Eco-friendly travel gear'):")
        product_name = st.text_input(
            "Enter the product name (if any, e.g., 'EcoTraveller Backpack'):")
        famous_style = st.text_input(
            "Optional: Enter a famous person's writing style you'd like to mimic (e.g., 'Ernest Hemingway'):")
        other_info = st.text_area(
            "Is there anything else you think might be helpful? (e.g., 'The product is made of 100% recycled materials.')")

        # When user presses "Enhance Prompt", make a call to GPT-4 for an improved prompt
        if st.button("Enhance Prompt"):
            # Build the conversation messages
            messages = [
                {"role": "system", "content": "You are a world-class prompt engineer."},
                {"role": "user", "content": f"Enhance this prompt based on the following parameters: Tone - {tone}, Target Market - {target_market}, Niche - {niche}, Product Name - {product_name}, Style - {famous_style}, Additional Information - {other_info}. The original prompt is: {desired_prompt}"}
            ]

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages
            )

            # Display the enhanced prompt
            enhanced_prompt = response['choices'][0]['message']['content']
            st.text_area("Enhanced Prompt:", value=enhanced_prompt, height=200)


if __name__ == "__main__":
    main()


# example prompt:
# create a prompt that will help me write a blog post about the best way to travel to Europe.
# The tone should be friendly and the target market is millennials.
# The niche is eco-friendly travel gear.
# The product name is EcoTraveller Backpack.
# The style is Ernest Hemingway.
# The product is made of 100% recycled materials.
