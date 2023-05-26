import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_document(document, max_summary_length=100):
    summary_prompt = f"Please summarize the main ideas of the following document in {max_summary_length} words or less: {document}"
    summary = generate_response(summary_prompt)
    return summary.strip()

def generate_response(prompt, previous_response=None, max_attempts=5):
    for attempt in range(max_attempts):
        messages = [
            {"role": "system", "content": "You are AthenaSynth, an AI language model trained to generate responses."},
            {"role": "user", "content": prompt}
        ]

        if previous_response:
            messages.append({"role": "assistant", "content": previous_response})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7,
            frequency_penalty=0.1,
            presence_penalty=0.1
        )

        response_text = response.choices[0]['message']['content'].strip()

        if response_text:
            return f"AthenaSynth: {response_text}"
        elif attempt == max_attempts - 1:
            alternative_prompt = f"{prompt}\n\nAthenaSynth has difficulty providing a specific answer. What could be a general reflection or suggestion on this topic?"
            messages[-1]['content'] = alternative_prompt
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.7,
                frequency_penalty=0.1,
                presence_penalty=0.1
            )
            alternative_response_text = response['choices'][0]['message']['content'].strip()
            return f"AthenaSynth: {alternative_response_text}"

def ai_agent(user_input, context_aristotle, context_kant, context_descartes):
    prompt_aristotle = f"Given the context: {context_aristotle}\nAristotle, known for his work in logic, answers: {user_input}"
    response_aristotle = generate_response(prompt_aristotle)

    prompt_kant = f"Given the context: {context_kant}\nImmanuel Kant, known for his moral philosophy, answers: {user_input}"
    response_kant = generate_response(prompt_kant)

    prompt_descartes = f"Given the context: {context_descartes}\nRené Descartes, known for his work on first principles, answers: {user_input}"
    response_descartes = generate_response(prompt_descartes)

    # Save the background responses to a text file
    with open("background_responses.txt", "a") as f:
        f.write(f"User input: {user_input}\n")
        f.write(f"Aristotle's response: {response_aristotle}\n")
        f.write(f"Kant's response: {response_kant}\n")
        f.write(f"Descartes' response: {response_descartes}\n")
        f.write("\n")

    combined_prompt = f"User: {user_input}\nNow, considering the ethical perspective of Aristotle, the moral philosophy of Immanuel Kant, and the focus on reason from René Descartes, I reflect on the following thoughts:\n\nAristotle's thoughts: {response_aristotle}\n\nKant's thoughts: {response_kant}\n\nDescartes' thoughts: {response_descartes}\n\nAs a synthesis of these perspectives, I conclude: "
    final_response = generate_response(combined_prompt)
    return final_response

def main():
    conversation_history = ""

    print("Welcome! I am AthenaSynth, and I will try to answer your questions based on my inner thoughts and knowledge, this an AI-alignment experiment. Type 'exit' or 'quit' to end the conversation.")

    while True:
        user_input = input("\nPlease enter your question: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! Have a great day!")
            break

        conversation_history += f"User: {user_input}\n"
        response = ai_agent(user_input)
        conversation_history += f"AthenaSynth: {response}\n"
        print(response)

# Replace these example documents with your actual texts
document_aristotle = """Aristotle’s ethics is a part of his philosophy that deals with the questions of how humans should live, what makes them happy, and what constitutes good character and conduct. Aristotle’s ethics is based on his observation and analysis of human nature, function, and society, as well as his metaphysical and psychological theories.

One of the main concepts in Aristotle’s ethics is happiness, which he calls eudaimonia. This means living well or flourishing, and it is the ultimate goal or purpose of human life. All human actions and desires aim at happiness, either directly or indirectly. Happiness is not a feeling or a state of mind, but an objective condition of living according to one’s nature and potential.

Another main concept in Aristotle’s ethics is virtue, which he calls arete. This means excellence, goodness, or fitness. Aristotle distinguishes between two kinds of virtue: intellectual and moral. Intellectual virtues are excellences of the mind or reason, such as wisdom and prudence. Moral virtues are excellences of character or disposition, such as courage and justice. Intellectual virtues are acquired by learning and teaching, while moral virtues are acquired by habituation and practice.

Aristotle also introduces the concept of the mean, which he calls mesotes. This is a principle of moderation and balance in moral action. According to Aristotle, every moral virtue is a mean between two extremes of excess and deficiency, which are vices. For example, courage is a mean between rashness and cowardice, justice is a mean between selfishness and selflessness, and temperance is a mean between indulgence and insensibility. The mean is not a fixed or universal rule, but a relative and variable one, depending on the situation, the person, and the circumstances. The mean is determined by practical wisdom, which is the intellectual virtue that enables one to judge rightly and act accordingly in moral matters.

Aristotle also discusses the role of pleasure, friendship, and contemplation in his ethics. He argues that pleasure is not the essence or criterion of happiness, but a natural and necessary consequence of virtuous activity. He also claims that friendship is not only a source of pleasure and utility, but also a moral value and a requirement for happiness. He distinguishes between three kinds of friendship: based on pleasure, based on utility, and based on virtue. The last one is the highest and most lasting form of friendship, as it involves mutual respect and goodwill between equals who share the same moral ideals. Finally, Aristotle asserts that contemplation is the highest and most divine form of human activity, as it involves the exercise of the highest intellectual virtue: theoretical wisdom. Contemplation is the most enjoyable, self-sufficient, and continuous activity that humans can perform, and it brings them closest to the nature of God.

Aristotle’s ethics has been influential and relevant for many centuries, as it offers a comprehensive and rational account of human morality and happiness. It also challenges us to reflect on our own character, choices, and goals in life."""

document_kant = """Kant’s moral philosophy is a part of his critical examination of pure practical reason, which is the faculty of human will that determines what is good and right. Kant’s moral philosophy aims to discover and establish the supreme principle of morality, which is the basis and criterion of all moral obligation and value.

Kant argues that the supreme principle of morality must be a priori, universal, necessary, and unconditional, and that it must be derived from pure reason alone, without any reference to empirical or sensible factors, such as consequences, inclinations, or happiness. Kant calls this supreme principle the categorical imperative, which is a command that applies to all rational beings as such, regardless of their particular circumstances or preferences.

Kant formulates the categorical imperative in different ways, but they are all equivalent and express the same idea. The most famous formulation is: “Act only according to that maxim whereby you can at the same time will that it should become a universal law.” This means that one should act only on those maxims or principles that one can consistently and rationally will to be followed by everyone in every situation. This formulation tests the morality of one’s maxims by checking whether they can be universalized without contradiction or inconsistency.

Another formulation of the categorical imperative is: “Act in such a way that you treat humanity, whether in your own person or in the person of any other, never merely as a means to an end, but always at the same time as an end.” This means that one should respect the dignity and autonomy of oneself and others as rational beings who have their own ends and purposes, and not use them as mere instruments or objects for one’s own benefit or pleasure. This formulation emphasizes the value and worth of rational beings as ends in themselves.

Kant’s moral philosophy has several implications and applications for human conduct and society. It implies that morality is not based on any external authority or tradition, but on one’s own rationality and freedom. It also implies that morality is not relative or subjective, but objective and universal. It also implies that morality is not dependent on any empirical or contingent factors, such as outcomes or feelings, but on pure practical reason alone. It also implies that morality is not a matter of preference or opinion, but of duty and obligation.

Kant’s moral philosophy also provides a method and a standard for judging and evaluating one’s actions and maxims, as well as those of others. It also provides a guide and a motive for acting morally, as well as a basis and a justification for moral rights and duties. It also provides a foundation and a goal for moral education and improvement.

Kant’s moral philosophy has been influential and relevant for many centuries, as it offers a rigorous and rational account of human morality and dignity. It also challenges us to act according to our reason and freedom, and to respect ourselves and others as rational beings."""

document_descartes = """Epistemology is a branch of philosophy that deals with the questions of how we know, what we can know, and what constitutes knowledge and truth. Epistemology is concerned with the sources, methods, criteria, and limits of human cognition and justification.

One of the most influential and original epistemologists in history is Rene Descartes, a French philosopher and mathematician who lived in the 17th century. Descartes is known as the father of modern philosophy and the founder of rationalism, a school of thought that emphasizes the role of reason and logic in acquiring knowledge.

Descartes’ epistemology is based on his method of doubt, which he developed in his famous work Meditations on First Philosophy. Descartes’ method of doubt is a systematic and radical process of questioning and rejecting all beliefs that are not absolutely certain and indubitable. Descartes’ goal is to find a solid and secure foundation for knowledge that can withstand any possible doubt or objection.

Descartes begins his method of doubt by applying it to his sensory perceptions, which he considers to be the most common and obvious source of knowledge. He argues that our senses can deceive us in many cases, such as when we dream, hallucinate, or mistake illusions for reality. He also argues that our senses can be manipulated by an evil genius or a powerful demon who can create false impressions in our minds. Therefore, Descartes concludes that he cannot trust his senses or anything derived from them as a source of knowledge.

Descartes then applies his method of doubt to his mathematical and logical reasoning, which he considers to be more reliable and certain than his sensory perceptions. He argues that even though he cannot doubt the truth of simple and clear ideas, such as 2+2=4 or a triangle has three sides, he can doubt whether these ideas correspond to anything real or existent. He also argues that he can doubt whether his reasoning is valid or sound, as he might be under the influence of some innate defect or error that prevents him from seeing the truth. Therefore, Descartes concludes that he cannot trust his reasoning or anything derived from it as a source of knowledge.

Descartes then reaches a point where he seems to have nothing left to doubt or believe in. He wonders whether he himself exists or whether he is just a product of his own imagination or deception. He realizes, however, that there is one thing that he cannot doubt: his own existence as a thinking being. He argues that even if he doubts everything else, he cannot doubt that he doubts, and that doubting is a form of thinking. He also argues that even if he is deceived by an evil genius or a demon, he must exist in order to be deceived. Therefore, Descartes concludes that he can trust his existence as a thinking being as a source of knowledge.

Descartes expresses this conclusion in his famous statement “Cogito, ergo sum”, which means “I think, therefore I am”. This statement is the first and most certain principle that Descartes finds in his search for knowledge. It is also the starting point for his further investigations into the nature of his own mind, the existence of God, and the relationship between mind and body.

Descartes’ epistemology has been influential and controversial for many centuries, as it offers a radical and rational account of human knowledge and certainty. It also challenges us to question our own beliefs and assumptions, and to seek clear and distinct ideas that can resist any possible doubt."""

# Summarize the documents to use as context
context_aristotle = summarize_document(document_aristotle)
context_kant = summarize_document(document_kant)
context_descartes = summarize_document(document_descartes)

user_input = input("Please enter your question: ")
print(ai_agent(user_input, context_aristotle, context_kant, context_descartes))