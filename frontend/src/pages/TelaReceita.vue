<template>
  <div class="container">
    <div class="row">
      <div class="card">
        <div class="card-content">
          <div class="text-column">
            <h4>Panquecas Veganas com Mel e Frutas</h4>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
              labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
              laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
              voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
              non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            <h4>INGREDIENTES</h4>
            <p>- 1 xícara de farinha de trigo;
              - 2 colheres de sopa de fermento em pó;
              - 1 xícara de leite vegetal;
              - 2 colheres de sopa de óleo vegetal;
              - 1 xícara de frango vegano desfiado;
              - 1 colher de sopa de extrato de tomate;
              - 1 dente de alho picado;
              - 2 colheres de sopa de cebola picada;
              - 1 xícara de mussarela vegana ralada;
              orégano à gosto.</p>
          </div>
          <div class="image-column">
            <img src="../assets/TestImage2.png" alt="Imagem Receita 1" />
            <img src="../assets/TestImage.png" alt="Imagem Receita 2" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'TelaReceita',
  components: {},
  data() {
    return {
      receita: {}
    }
  },
  methods: {
    buscaReceitaPorId(){
      this.receita = {
        titulo:"add",
        ingredientes:["ssssssss"],
        instrucoes:"aaaaaaas",
        categorias:["JANTAR"],
        tags:["PORCO"],
        files:[]
      }
    }
  },
  mounted(){
    this.buscaReceitaPorId()
  }
}
</script>
<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.card {
  width: 1026px;
  height: 750px;
  border-radius: 25px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
}

.card-content {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.text-column {
  flex: 1;
  padding-right: 20px;
}

.image-column {
  flex: 1;
}

/* Estilos para a imagem, ajuste conforme necessário */
.image-column img {
  max-width: 100%;
  height: auto;
}

h4 {
  color: #222;
  font-family: Roboto;
  font-size: 30px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  margin: 22px 40px;
}

p {
  color: #000;
  font-family: Roboto;
  font-size: 20px;
  font-style: normal;
  font-weight: 200;
  line-height: normal;
  margin: 22px 40px;
  text-align: justify;
}

img {
  width: 100%;
  height: calc(50% - 15px);
  object-fit: cover;
  margin-bottom: 15px;
}
</style>

    