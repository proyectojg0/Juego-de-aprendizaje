document.addEventListener('DOMContentLoaded', () => {
    const RENDER_PROXY_URL = "https://proyecto-jg.onrender.com";

    const quizData = {
        algebra: [
            { q: "Cual es el valor de x en 2x = 10", o: ["3", "5", "10", "2"], a: 1 },
            { q: "Que es una incognita", o: ["Una variable", "Un numero", "Una suma", "Un signo"], a: 0 },
            { q: "5 + 3 \u00B7 2 = ", o: ["16", "11", "10", "8"], a: 1 },
            { q: "Que es una ecuacion", o: ["Igualdad", "Restar", "Multiplicar", "Variable"], a: 0 },
            { q: "Si x=4 3x = ", o: ["3", "7", "12", "8"], a: 2 },
            { q: "Que es un polinomio", o: ["Suma de terminos", "Numero primo", "Raiz", "Fraccion"], a: 0 },
            { q: "3\u00B2 = ", o: ["6", "9", "3", "12"], a: 1 },
            { q: "Una recta es", o: ["Curva", "Infinita", "Finita", "Variable"], a: 1 },
            { q: "x+x+x = ", o: ["2x", "5x", "3x", "x\u00B2"], a: 2 },
            { q: "Que es factorizar", o: ["Sumar", "Reducir", "Multiplicar", "Descomponer"], a: 3 },
            { q: "2(x+3) = ", o: ["2x+6", "2x+3", "x+5", "6x"], a: 0 },
            { q: "Derivada de x\u00B2", o: ["2x", "x", "x\u00B2", "3x"], a: 0 },
            { q: "Que es una raiz", o: ["Resultado", "Solucion", "Numero negativo", "Angulo"], a: 1 },
            { q: "7 \u00B7 0 = ", o: ["7", "0", "1", "No existe"], a: 1 },
            { q: "El opuesto de 5 es", o: ["-5", "5", "1/5", "5\u00B2"], a: 0 },
            { q: "Que es dominio", o: ["Entrada", "Salida", "Raiz", "Angulo"], a: 0 },
            { q: "2\u00B3 = ", o: ["6", "8", "9", "4"], a: 1 },
            { q: "Si 4/x = 2 \u2192 x = ", o: ["2", "8", "3", "4"], a: 0 },
            { q: "Que es un sistema", o: ["Ecuaciones juntas", "Un numero", "Suma", "Angulo"], a: 0 },
            { q: "Que es |x|", o: ["Valor Absoluto", "Raiz", "Funcion", "Variable"], a: 0 }
        ],
        filosofia: [
            { q: "Quien dijo Solo se que no se nada", o: ["Socrates", "Platon", "Aristoteles", "Kant"], a: 0 },
            { q: "La filosofia estudia", o: ["La verdad", "Los mapas", "La quimica", "La musica"], a: 0 },
            { q: "Que es etica", o: ["Problemas", "Conducta correcta", "Arte", "Ciencia"], a: 1 },
            { q: "Platon creo", o: ["El mito de la caverna", "El telefono", "La rueda", "El libro"], a: 0 },
            { q: "Que es pensar", o: ["Memorizar", "Reflexionar", "Dormir", "Hablar"], a: 1 },
            { q: "Aristoteles fue alumno de", o: ["Kant", "Nietzsche", "Platon", "Descartes"], a: 2 },
            { q: "La logica estudia", o: ["Belleza", "Razon", "Arte", "Tiempo"], a: 1 },
            { q: "Que es moral", o: ["Reglas sociales", "Comer", "Escribir", "Viajar"], a: 0 },
            { q: "La filosofia nace en", o: ["China", "Grecia", "Roma", "India"], a: 1 },
            { q: "Que es duda", o: ["Certeza", "Investigacion", "Inseguridad", "Confianza"], a: 2 },
            { q: "Kant hablo de", o: ["Razon", "Tierra", "Electricidad", "Animales"], a: 0 },
            { q: "Que es libertad", o: ["Obedecer", "Elegir", "Repetir", "Copiar"], a: 1 },
            { q: "Nietzsche hablo del", o: ["Superhombre", "Atomo", "Cielo", "Sol"], a: 0 },
            { q: "Que es verdad", o: ["Opinion", "Realidad", "Palabra", "Arte"], a: 1 },
            { q: "El mito de la caverna trata de", o: ["Ignorancia", "Viajes", "Animales", "Espejos"], a: 0 },
            { q: "Descartes dijo", o: ["Pienso luego existo", "Vivo de amor", "Veo y creo", "Llueve"], a: 0 },
            { q: "Que es argumento", o: ["Razon", "Grito", "Cosa", "Sueño"], a: 0 },
            { q: "Estoicismo enseña", o: ["Control emocional", "Fuerza fisica", "Magia", "Canto"], a: 0 },
            { q: "Que es duda metodica", o: ["Todo se analiza", "Comer", "Correr", "Dormir"], a: 0 },
            { q: "Heraclito dijo", o: ["Todo fluye", "Nada cambia", "Solo cae", "Todo es igual"], a: 0 }
        ],
        desarrollo: [
            { q: "Que es autoestima", o: ["Valor propio", "Fuerza", "Memoria", "Notas"], a: 0 },
            { q: "Dormir bien ayuda a", o: ["Motivacion", "Odio", "Estres", "Pereza"], a: 0 },
            { q: "La meta es", o: ["Objetivo", "Problema", "Frase", "Juego"], a: 0 },
            { q: "Que es disciplina", o: ["Constancia", "Correr", "Forzar", "Gritar"], a: 0 },
            { q: "El estres se reduce con", o: ["Respirar", "Gritar", "Ignorar", "Pelear"], a: 0 },
            { q: "Habito es", o: ["Repeticion", "Comida", "Ropa", "Juego"], a: 0 },
            { q: "Organizar ayuda a", o: ["Rendir mejor", "Cansarte", "Olvidar", "Fallar"], a: 0 },
            { q: "Que es motivacion", o: ["Impulso", "Descripcion", "Letra", "Fuerza"], a: 0 },
            { q: "Leer mejora", o: ["Atencion", "Problemas", "Sueño", "Hambre"], a: 0 },
            { q: "Responsabilidad implica", o: ["Cumplir", "Evitar", "Huir", "Ignorar"], a: 0 },
            { q: "Perseverar es", o: ["Rendirse", "Seguir", "Esperar", "Olvidar"], a: 1 },
            { q: "Un lider", o: ["Inspira", "Grita", "Ordena", "Ignora"], a: 0 },
            { q: "Empatia es", o: ["Ponerse en lugar del otro", "Correr", "Hablar", "Dormir"], a: 0 },
            { q: "Habitos malos generan", o: ["Problemas", "Salud", "Exito", "Risa"], a: 0 },
            { q: "Ser puntual muestra", o: ["Respeto", "Miedo", "Sueño", "Hambre"], a: 0 },
            { q: "Leer 10 min diarios es", o: ["Habito", "Juego", "Plan", "Meta"], a: 0 },
            { q: "Que es autoconocimiento", o: ["Entenderse", "Dormir", "Caminar", "Cantar"], a: 0 },
            { q: "Tomar agua mejora", o: ["Cuerpo", "Ruido", "Clima", "Arte"], a: 0 },
            { q: "Rutina sana implica", o: ["Habitos buenos", "No hacer nada", "Comer mal", "Pelear"], a: 0 },
            { q: "Que es resiliencia", o: ["Superar dificultades", "Correr", "Saltar", "Leer"], a: 0 }
        ]
    };

    let currentQuiz = [];
    let currentQuestionIndex = 0;
    let score = 0;
    let currentCategoryName = "";

    const title = document.getElementById('page-title');
    const mainMenu = document.getElementById('main-menu');
    const startMenu = document.getElementById('start-menu');
    const aiMenu = document.getElementById('ai-menu');
    const quizMenu = document.getElementById('quiz-menu');
    const feedbackOverlay = document.getElementById('feedback-overlay');
    const infoBtn = document.getElementById('info-btn');
    const infoModal = document.getElementById('info-modal');
    const closeModal = document.getElementById('close-modal');
    
    const quizQuestion = document.getElementById('quiz-question');
    const quizOptionsContainer = document.getElementById('quiz-options');
    const btnFinishQuiz = document.getElementById('btn-finish-quiz');

    const btnIniciar = document.getElementById('btn-iniciar');
    const btnRegresar = document.getElementById('btn-regresar');
    const quizCategoryButtons = document.querySelectorAll('.quiz-btn');
    const btnAIHelp = document.getElementById('btn-ai-help');
    const btnRegresarAI = document.getElementById('btn-regresar-ai');
    const btnSendAI = document.getElementById('btn-send-ai');
    const userInput = document.getElementById('user-input');
    const chatOutput = document.getElementById('chat-output');

    function switchMenu(showMenu, titleText) {
        [mainMenu, startMenu, aiMenu, quizMenu].forEach(menu => {
            menu.classList.add('hidden');
        });
        showMenu.classList.remove('hidden');
        title.textContent = titleText;
        btnFinishQuiz.classList.add('hidden');
    }

    function formatCategoryName(category) {
        let name = category.charAt(0).toUpperCase() + category.slice(1);
        name = name.replace(/[.,]/g, ''); 
        return name;
    }

    function updateQuizTitle() {
        const categoryDisplay = formatCategoryName(currentCategoryName);
        const progressDisplay = `${currentQuestionIndex + 1}/${currentQuiz.length}`;
        title.textContent = `${categoryDisplay} (${progressDisplay})`;
    }

    function startQuiz(category) {
        currentQuiz = quizData[category];
        currentQuestionIndex = 0;
        score = 0;
        currentCategoryName = category;
        switchMenu(quizMenu, "Cargando");
        loadQuestion();
    }

    function loadQuestion() {
        if (currentQuestionIndex >= currentQuiz.length) {
            showResults();
            return;
        }

        updateQuizTitle();

        const q = currentQuiz[currentQuestionIndex];
        quizQuestion.textContent = q.q;
        quizOptionsContainer.innerHTML = '';
        
        q.o.forEach((option, index) => {
            const button = document.createElement('button');
            button.className = 'btn secondary-btn quiz-option';
            button.textContent = option;
            button.onclick = () => handleAnswer(index, q.a);
            quizOptionsContainer.appendChild(button);
        });
    }

    function handleAnswer(selectedIndex, correctAnswerIndex) {
        const isCorrect = selectedIndex === correctAnswerIndex;

        feedbackOverlay.classList.remove('hidden', 'correct', 'incorrect');
        if (isCorrect) {
            score++;
            feedbackOverlay.classList.add('correct');
        } else {
            feedbackOverlay.classList.add('incorrect');
        }
        
        document.querySelectorAll('.quiz-option').forEach(btn => btn.disabled = true);

        currentQuestionIndex++;
        
        setTimeout(() => {
            feedbackOverlay.classList.add('hidden');
            loadQuestion();
        }, 800);
    }

    function showResults() {
        title.textContent = "Resultados";
        quizQuestion.textContent = `Quiz Terminado ${formatCategoryName(currentCategoryName)}`;
        quizOptionsContainer.innerHTML = `<p>Tu puntuacion final es ${score} de ${currentQuiz.length}</p>`;
        btnFinishQuiz.classList.remove('hidden');
    }

    btnIniciar.addEventListener('click', () => {
        switchMenu(startMenu, "Elije una categoria");
    });

    quizCategoryButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            startQuiz(e.target.dataset.category);
        });
    });

    btnRegresar.addEventListener('click', () => {
        switchMenu(mainMenu, "Juego de Aprendizaje");
    });
    
    btnFinishQuiz.addEventListener('click', () => {
        switchMenu(mainMenu, "Juego de Aprendizaje");
    });

    infoBtn.addEventListener('click', () => {
        infoModal.classList.remove('hidden');
    });

    closeModal.addEventListener('click', () => {
        infoModal.classList.add('hidden');
    });

    infoModal.addEventListener('click', (e) => {
        if (e.target === infoModal) {
            infoModal.classList.add('hidden');
        }
    });
    
    btnAIHelp.addEventListener('click', () => {
        switchMenu(aiMenu, "Ayuda con IA");
    });

    btnRegresarAI.addEventListener('click', () => {
        switchMenu(mainMenu, "Juego de Aprendizaje");
    });

    async function sendQueryToGemini() {
        const question = userInput.value.trim();
        if (!question) return;

        chatOutput.innerHTML += `<p class="user-message">Tu ${question}</p>`;
        userInput.value = '';
        btnSendAI.disabled = true;

        chatOutput.innerHTML += `<p id="loading-message" class="ai-message">Escribiendo respuesta</p>`;
        chatOutput.scrollTop = chatOutput.scrollHeight; 

        const payload = {
            question: question
        };

        try {
            const response = await fetch(RENDER_PROXY_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `Error HTTP ${response.status}`);
            }

            const data = await response.json();
            const aiResponse = data.response;

            const loading = document.getElementById('loading-message');
            if (loading) loading.remove();

            chatOutput.innerHTML += `<p class="ai-message">IA ${aiResponse}</p>`;

        } catch (error) {
            console.error("Error al llamar al proxy de Render", error);
            const loading = document.getElementById('loading-message');
            if (loading) loading.remove();
            chatOutput.innerHTML += `<p class="error-message">Error de conexión: ${error.message}</p>`;
        } finally {
            btnSendAI.disabled = false;
            chatOutput.scrollTop = chatOutput.scrollHeight;
        }
    }

    btnSendAI.addEventListener('click', sendQueryToGemini);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendQueryToGemini();
        }
    });
});
