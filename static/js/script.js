async function getReport() {
  const city = document.getElementById("cityInput").value;
  const res = await fetch(`/report?city=${city}`);
  const data = await res.json();
  document.getElementById("result").innerText = data.recommendation;
}
