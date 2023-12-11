<template>
  <div class="container">
    <div class="card">
      <div class="text-column">
        <div class="recipe-info">
          <h4>{{ receita.titulo }}</h4>
          <p>{{ receita.instrucoes }}</p>
        </div>
        <div class="ingredientes">
          <h4>INGREDIENTES</h4>
          <ul>
            <li v-for="(ingrediente, index) in receita.ingredientes" :key="index">
              {{ ingrediente }}
            </li>
          </ul>
        </div>
      </div>
      <div class="image-column">
        <template v-if="receita.fotos && receita.fotos.length">
          <img v-for="(foto, index) in receita.fotos" :src="transformarPath(foto)" :key="index" alt="Imagem Receita" />
        </template>
        <template v-else>
          <p>Carregando...</p>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { searchById } from 'src/services/recipe'


export default {
  name: 'TelaReceita',
  props: {
    titulo: String,
    ingredientes: String,
    instrucoes: String,
    foto: String
  },
  components: {},
  data() {
    return {
      receita: {}
    }
  },
  methods: {
    buscaReceitaPorId(receitaId) {
      searchById({ receita_id: receitaId })
        .then(({ data }) => {
          this.receita = data
          console.log(data)
          console.log(data.foto)
        })
        .catch(error => {
          console.error('Erro ao buscar receita por ID:', error)
        })
    },
    transformarPath(uploads) {
      const backendURL = 'http://localhost:5000'
      const nomeArquivo = uploads.substring(uploads.lastIndexOf('/') + 1)

      return `${backendURL}/images/${nomeArquivo}`
    }
  },
  mounted() {
    const idDaReceita = this.$route.query.id
    this.buscaReceitaPorId(idDaReceita)
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
  width: 100%;
  max-width: 1026px;
  border-radius: 25px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  overflow: hidden;
}

.card-content {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.text-column {
  flex: 1;
  padding-right: 20px;
  box-sizing: border-box;
}

.image-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  box-sizing: border-box;
}

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