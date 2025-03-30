![image](https://github.com/user-attachments/assets/342bad58-9445-43f0-976e-59dfa0ec38bd)# Modern ChatGPT Clone

A fully-functional ChatGPT-style web application built with Django and Groq API. This project serves as a starting point for developers looking to create their own AI chat applications with customized features.
![image](https://github.com/user-attachments/assets/c9453188-abe4-4963-ad0b-f724a0af615d)
![image](https://github.com/user-attachments/assets/4050c667-bbf8-4c85-92e9-35ef8fcf1e50)
![image](https://github.com/user-attachments/assets/5c055d39-b310-439d-a045-4c5d1b28a6ce)
![image](https://github.com/user-attachments/assets/ee46681b-f059-4600-91c3-5d21a7dabd88)
![image](https://github.com/user-attachments/assets/006ac2cb-732e-45ce-8cd7-4fbbb67632fe)
![image](https://github.com/user-attachments/assets/42698085-bd06-48b2-af9d-07d2858e972d)

## Features

- 🚀 Real-time streaming responses
- 🎨 Modern, responsive UI with cyberpunk theme
- 📁 File upload and processing capabilities
- 👤 User authentication and profile management
- 💾 Chat history and management
- 🔒 Secure JWT authentication
- 📱 Mobile-friendly design

## Tech Stack

- Django 5.1.7
- Groq API
- TailwindCSS
- JavaScript (Vanilla)
- SQLite (can be configured for other databases)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/chatgpt-clone.git
cd chatgpt-clone
```

2. Create and activate virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
JWT_SECRET=your_jwt_secret_key_here
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=1440 (or your desired number)
JWT_REFRESH_TOKEN_EXPIRE_MINUTES=30
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser (admin):

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the application in action!

## Customization

### Changing the AI Model

- You can update the `SYSTEM_PROMPT` in `chat/views.py`
- Or Change the `self.default_model` in `chat/ai_models.py` to your desired model from GROQ

### Adding Features

1. Create new models in `models.py`
2. Add views in `views.py`
3. Create templates in `templates/`
4. Update URLs in `urls.py`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/SomeFeature`)
3. Commit your changes (`git commit -m 'Add SomeFeature'`)
4. Push to the branch (`git push origin feature/SomeFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you find this project helpful, please give it a ⭐️ on GitHub!

For issues, questions, or contributions, please open an issue or PR.

---
