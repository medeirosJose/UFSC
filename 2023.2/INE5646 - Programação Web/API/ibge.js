
const selectUF = document.querySelector('#uf');
const selectMunicipios = document.querySelector('#municipios');

function populateUF() {
    fetch("https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome")
        .then(res => res.json())
        .then(uf => {

            uf.map(uf => {

                const option = document.createElement('option');

                option.setAttribute('value', uf.sigla);
                option.textContent = uf.sigla;

                selectUF.appendChild(option);
            });

            // Adicione um evento de escuta para o elemento selectUF após populá-lo
            selectUF.addEventListener('change', function () {
                const selectedUF = selectUF.value;
                populateMunicipios(selectedUF);
            });
        });
}

populateUF();

function populateMunicipios(UF) {
    fetch(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${UF}/municipios`)
        .then(res => res.json())
        .then(municipios => {

            document.getElementById('municipios').innerHTML = '';
            municipios.map(municipio => {

                const option = document.createElement('option');

                option.setAttribute('value', municipio.nome);
                option.textContent = municipio.nome;

                selectMunicipios.appendChild(option);
            });
        });
}

