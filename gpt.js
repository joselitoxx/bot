
function getResponse() {
// Obtener la pregunta del área de texto
const promptText = document.getElementById('input').value;

fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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',
  },
  body: JSON.stringify({
    prompt: promptText,
    temperature: 0.7,
    max_tokens: 100,
    n: 1,
    stop: '\n'
  })
})
  .then(response => response.json())
  .then(data => {
    // Verificar si la propiedad choices existe en los datos
    if (data.choices && data.choices.length > 0) {
      // Acceder a la primera opción de respuesta
      const responseText = data.choices[0].text;
      // Hacer algo con la respuesta
      console.log(responseText);
    } else {
      console.log('No se encontraron respuestas');
    }
  })
  .catch(error => console.error(error));
}


const myTextarea = document.getElementById("txtMsg");

myTextarea.addEventListener("input", () => {
  myTextarea.style.height = "auto";
  myTextarea.style.height = myTextarea.scrollHeight + "px";
});
