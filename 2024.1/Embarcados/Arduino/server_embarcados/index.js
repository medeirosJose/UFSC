const express = require("express");
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Página inicial do servidor!");
  console.log("usuario logou");
});

let counter = 0;

app.post("/receber_temp", (req, res) => {
  const { currentTemp } = req.body;
  console.log("[!] <- Temperatura no Thermistor:", currentTemp, "°C");
});

app.get("/enviar_params", (req, res) => {
  const dangerTemp = 222;
  const safeTemp = 100;
  counter += 1;
  console.log(
    "\n\n[Log ", counter,"] -> Enviando valores. Perigo:", dangerTemp," Seguro:",safeTemp,"")
  res.send({ dangerTemp, safeTemp });
});

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});r
