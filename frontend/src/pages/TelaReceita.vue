<template>
  <div class="column">
    <div class="secao-voltar canto-esquerdo" @click="voltarBusca">
      <q-icon class="q-mt-xs icone-triangulo" name="mdi-arrow-left-circle"></q-icon>
      <a class="botao-voltar"> Voltar</a>
    </div>
    <div class="container">
      <div class="card">
        <div class="text-column justify-between column">
          <div>
            <div class="q-pl-md">
              <h4>{{ receita.titulo }}</h4>
            </div>
            <div class="ingredientes">
              <h6>INGREDIENTES</h6>
              <ul v-for="(ingrediente, index) in listaIngrediente" :key="index" style="padding-left: 60px">
                <li>
                  {{ ingrediente }}
                </li>
              </ul>
              <div>
                <h6>MODO DE PREPARO:</h6>
                <p>{{ receita.instrucoes }}</p>
              </div>
            </div>
          </div>
          <div class="row justify-end">
            <div @click="compartilhar" class="row q-ml-lg q-mb-lg cursor-pointer">
              <q-icon class="icone-filtro.self-center" name="mdi-content-copy" size="20px"></q-icon>
              <span class="q-pl-sm">Copiar link</span>
            </div>
            <div @click="salvarPDF" class="row q-ml-lg q-mb-lg cursor-pointer">
              <q-icon class="icone-filtro.self-center" name="mdi-file-pdf-box" size="20px"></q-icon>
              <span class="q-pl-sm">Salvar PDF</span>
            </div>
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
  </div>
</template>

<script>
import { searchById } from 'src/services/recipe'
import { mapGetters } from 'vuex'


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
      receita: {},
      listaIngrediente: []
    }
  },
  computed: {
    ...mapGetters('busca', ['parametrosBusca'])
  },
  methods: {
    buscaReceitaPorId(receitaId) {
      searchById({ receita_id: receitaId })
        .then(({ data }) => {
          this.receita = data
          this.transformToList()
        })
        .catch(error => {
          console.error('Erro ao buscar receita por ID:', error)
          this.triggerMensagem('positive', 'Erro ao buscar receita.')
        })
    },
    transformarPath(uploads) {
      const backendURL = 'https://gastroweb.onrender.com'
      const nomeArquivo = uploads.substring(uploads.lastIndexOf('/') + 1)

      return `${backendURL}/images/${nomeArquivo}`
    },
    transformToList() {
      if (!(this.receita.ingredientes === undefined)) {
        if (this.receita.ingredientes[0].trim() === '') {

          this.listaIngrediente = []
        } else {
          const lista = this.receita.ingredientes[0].split(',')

          this.listaIngrediente = lista.map(item => item.trim())
        }
      }
    },
    compartilhar() {
      navigator.clipboard.writeText(window.location.href)
      this.triggerMensagem('positive', 'Link copiado.')
    },
    triggerMensagem(type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
      })
    },
    salvarPDF() {
      const conteudo = this.$refs.conteudoParaImprimir
      window.print()
    },
    voltarBusca() {
      const query = {
        ...this.parametrosBusca,
        id: 0
      }
      console.log(this.parametrosBusca)
      if (this.parametrosBusca.titulo === '' || this.parametrosBusca.tags === [] || this.parametrosBusca.categorias === []) {
        this.$router.push({
          path: '/'
        })
      } else {
        const path = '/receitas'
        this.$router.push({ path, query })
      }
    }
  },
  watch: {
    'parametrosBusca.id'() {
      const idDaReceita = this.$route.query.id
      this.buscaReceitaPorId(idDaReceita)
    }
  },
  mounted() {
    const idDaReceita = this.$route.query.id
    this.buscaReceitaPorId(idDaReceita)
  }
}
</script>
<style scoped>
.ingredientes {
  font-family: Roboto;
  font-size: 20px;
  font-style: normal;
  font-weight: 200;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.card {
  width: 100%;
  max-width: 1026px;
  border-radius: 25px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  overflow: hidden;
  margin: 70px;
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

h6 {
  color: #222;
  font-family: Roboto;
  font-size: 23px;
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

.secao-voltar {
  display: flex;
  gap: 5px;
  cursor: pointer;
}

.botao-voltar {
  font-weight: 700;
  color: white;
  font-size: 15px;
  height: 20px;
  text-decoration: none;
}

.icone-triangulo {
  color: white;
  size: 50px;
}

.canto-esquerdo {
  display: flex;
  justify-content: flex-start;
  padding: 48px 0px 0px 48px;
}
</style>