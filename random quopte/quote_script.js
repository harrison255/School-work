async function getQuote() {
    try {
        let response = await fetch("http://127.0.0.1:5000/quote");
        let data = await response.json();
        document.getElementById("quote").innerText = data.text;
        document.getElementById("author").innerText = "~ " + data.author;
    } catch (err) {
        console.error("Error fetching quote:", err);
    }
}

window.onload = getQuote;
document.querySelector(".quote_btn").addEventListener("click", getQuote);
