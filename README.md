# Nom Nom README
## Inspiration
Ever found yourself in a college dorm with a handful of random groceries and no clue what to cook? NomNom is here to revolutionize your culinary experience. Our app combines cutting-edge technology with user-friendly features to bring you a hassle-free solution for your college kitchen conundrums. With NomNom, you can effortlessly scan your grocery items using OCR or manually input them, and watch as our advanced Language Model whips up creative and delicious recipes tailored to your available ingredients. No more staring blankly into the fridge – NomNom transforms your eclectic mix of groceries into mouthwatering meals. Embrace the simplicity, savor the creativity, and let NomNom redefine your college cooking journey. Our recipes will definitely make you go Nom Nom!

## What it does
NomNom takes in grocery items through two methods. The first involves a streamlined manual grocery input mechanism facilitated by a dynamic data frame editor, providing users with an efficient interface for seamless management and modification of their grocery lists. For those seeking an even more automated approach, NomNom leverages cutting-edge Optical Character Recognition (OCR) technology to transform physical receipts into a structured digital inventory.

Next, users can specify the quantity of their groceries as necessary, and our GPT-3.5-backed NomNom chatbot can recommend recipes based on the ingredients it sees in your inputted groceries. 

## How we built it
NomNom leverages the Streamlit framework for its front end, providing an efficient and user-friendly interface. The OCR functionality is powered by Hugging Face's EasyOCR model, delivering precise data extraction from grocery receipts. The backbone of recipe generation is OpenAI's GPT-4 API, a robust Large Language Model (LLM) known for its advanced natural language processing capabilities. This technical stack enables NomNom to seamlessly integrate manual and OCR-based grocery input methods, culminating in a streamlined user experience and personalized recipe suggestions based on precise ingredient quantities.

## Challenges we ran into
The main challenge we ran into was adjusting the layouts with Streamlit. Streamlit doesn't currently support chatbot integration into tabs, columns, or expanders. This greatly hindered our methods of integrating the chatbot alongside our OCR/manual grocery integration features.

## Accomplishments that we're proud of
We take pride in the successful implementation of our chatbot, which demonstrates a high level of sophistication in considering user-specific factors. Our system adeptly addresses food allergies and aligns with user preferences, particularly in terms of desired cuisines. This accomplishment showcases the effectiveness of our solution in tailoring responses to meet individual dietary needs and culinary preferences, enhancing the overall user experience.

## What we learned
Through this project, we've gained hands-on experience in integrating multiple technologies to address real-world problems. Working with Streamlit provided insights into creating interactive and visually appealing user interfaces, while Hugging Face's EasyOCR demonstrated the potential of Optical Character Recognition for extracting valuable information from images, specifically grocery receipts in our case. The utilization of OpenAI's GPT-4 API enhanced our understanding of implementing advanced Language Models for natural language processing tasks. This project has equipped us with the skills to build a comprehensive solution that combines different technologies cohesively to improve the user experience in a practical scenario.

## What's next for Nom Nom! - AI-Backed Recipe Generator
Our future plans for Nom Nom! - AI-Backed Recipe Generator involve broadening our reach to include students nationwide and extending support to individuals in underserved communities with limited resources. We aspire to collaborate with grocery stores and delivery services to offer enhanced utility for their users, empowering them to optimize their grocery purchases. Our commitment is to make the app more accessible and beneficial for a diverse range of users, fostering a community that thrives on creative and efficient cooking solutions.
