# 🎮 Tic Tac Toe with Reinforcement Learning (Q-Learning)

This is a web-based Tic Tac Toe game where a reinforcement learning agent trained using **Q-learning** plays against the user. The agent has been trained through self-play to learn optimal strategies and make intelligent decisions.



---

## 🚀 Live Demo

🟢 [Click here to play]([https://your-app-name.onrender.com](https://tic-tac-toe-with-reinforcement-learning.onrender.com/))  
*https://tic-tac-toe-with-reinforcement-learning.onrender.com/*


---
## 🖼️ Demo
![Screenshot 2025-07-06 161056](https://github.com/user-attachments/assets/945d5417-139c-4530-9155-2423394dec63)

![Screenshot 2025-07-06 161113](https://github.com/user-attachments/assets/f586e25a-6dda-4764-86cc-ff3ea8f3d4c2)

![Screenshot 2025-07-06 161136](https://github.com/user-attachments/assets/b9a69cf2-8791-4b0d-977f-ae11fa309e30)

![Screenshot 2025-07-06 161214](https://github.com/user-attachments/assets/a89bb304-73d8-4d41-824f-33234104ec28)

![Screenshot 2025-07-06 162122](https://github.com/user-attachments/assets/28a1b081-72da-491e-92ff-556ef612cd41)

---

## 🧠 How It Works

- The backend is built using **Django** (Python).
- The reinforcement learning agent uses the **Q-learning algorithm** to select the best move.
- Two modes are available:
  - **Agent Plays First** – Trained on **500,000 games**
  - **Agent Plays Second** – Trained on **100,000 games**
- The agent uses a precomputed **Q-table** stored as a `.pkl` file.

---

## 📊 Q-Learning Update Formula

The Q-values are updated using the following formula:

 Q(s, a) = Q(s, a) + α [ r + γ × max<sub>a'</sub> Q(s', a') − Q(s,a) ] 

Where:
- `Q(s, a)` is the current Q-value of state `s` and action `a`
- `α` is the learning rate
- `γ` is the discount factor
- `r` is the reward received
- `s'` is the next state
- `a'` is the next possible action



---

## 🛠️ Technologies Used

- Python 3
- Django
- HTML5, CSS3, JavaScript
- Bootstrap 5 (for styling)
- NumPy (for board matrix)
- Pickle (for loading the Q-table)

---

## 🧩 Features

- Two modes: Agent-first and Agent-second
- Q-table based agent — no neural network needed
- Bootstrap UI with clickable board
- Visual win line when game is won
- Highlighted win cells and game alerts
- Status messages (e.g., "Agent is thinking...")

---

## ⚙️ Deployment on Render

To deploy the project on [Render](https://render.com):

1. Create a new Web Service.
2. Connect your GitHub repo.
3. Use the following settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn yourprojectname.wsgi:application`
   - **Environment:** Python 3
4. Add environment variables:
   - `SECRET_KEY`
   - `DEBUG=false`
5. Add your Render domain to `ALLOWED_HOSTS` in `settings.py`.

---

## 📁 File Structure (Simplified)
Tic-Tac-Toe-With-Reinforcement-Learning-Q-learning-/

│

├── ticTactoe/

│ ├── views.py

│ ├── q_table_# Agent play move first #500000.pkl

│ ├── q_table_# Agent play move second 100000.pkl

│ └── ...

│

├── templates/

│ └── index.html

│ └── agentmovesecond.html

├── requirements.txt

├── model.py       #  This file contain raw project prepare in google colab

├── modelComponents.py

├── manage.py

└── README.md
## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/priyamghorui/Tic-Tac-Toe-With-Reinforcement-Learning-Q-learning-.git
```
2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**

```bash
Install Dependencies
pip install -r requirements.txt
```
4. **Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```
5. **Run the Server**

```bash
python manage.py runserver
```
# Thank You

