<template>
    <div class="container">
        <div class="row">
            <div class="card">
                <div class="card-content">
                    <div class="image-column">
                        <img src="../assets/TestImage2.png" alt="Imagem Receita" />
                    </div>
                    <div class="text-column">
                        <h4>Panquecas Veganas com Mel e Frutas</h4>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                            labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
                            laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
                            voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.card {
    width: 800px;
    height: 400px;
    border-radius: 25px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
}

.card-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.text-column {
    flex: 1;
    padding: 0 20px;
}

.image-column {
    flex: 1;
    display: flex;
    justify-content: center;
    margin: 0px 20px;
}

/* Estilos para a imagem, ajuste conforme necessário */
.image-column img {
    max-width: 100%;
    height: auto;
    margin: 22px 0;
}

h4 {
    color: #222;
    font-family: Roboto;
    font-size: 30px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    margin: 22px 0;
}

p {
    color: #000;
    font-family: Roboto;
    font-size: 20px;
    font-style: normal;
    font-weight: 200;
    line-height: normal;
    margin: 22px 0;
}
</style>