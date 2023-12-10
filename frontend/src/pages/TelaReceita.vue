<template>
  <div class="container">
    <div class="row">
      <div class="card">
        <div class="card-content">
          <div class="text-column">
            <h4>{{ titulo }}</h4>
            <p>{{ instrucoes }}</p>
            <h4>INGREDIENTES</h4>
            <p>{{ ingredientes }}</p>
          </div>
          <div class="image-column">
            <img :src="`/backend/${foto}`" alt="Imagem Receita" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { searchById } from 'src/services/recipe'
import { mapGetters } from 'vuex'


export default {
  name: 'TelaReceita',
  components: {},
  props: {
    titulo: String,
    id: Number,
    instrucoes: String,
    ingredientes: String,
    foto: String
  },
  data() {
    return {
      receita: {}
    }
  },
  computed: {
    ...mapGetters('busca', ['parametrosBusca'])
  },
  methods: {
    buscaReceitaPorId() {
      console.log(this.parametrosBusca.id)
      searchById({
        id: this.parametrosBusca.id
      }).then(({ data }) => {
        this.receita = data
        this.triggerMensagem('positive', 'Receita encontrada.')
        this.loading = false
      }).catch(error => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível encontrar receita.')
      })
      // this.receita = {
      //   titulo:'add',
      //   ingredientes:['ssssssss'],
      //   instrucoes:'aaaaaaas',
      //   categorias:['JANTAR'],
      //   tags:['PORCO'],
      //   files:[]
      // }
    }
  },
  mounted() {
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

    