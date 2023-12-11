<template lang="pug">
q-page
  section.q-pa-xl.column
    div.caixa-branca.column
      h4 Página de Administrador
      q-btn(@click="mudarPagina" color="black" text-color="white" no-caps).btn Criar Receita
    h4.q-pt-lg Editar Receitas Existentes:
    div.column.items-center
      div(v-for="(receita, index) in listaReceita").column
        CardReceita(:id="receita.id" :titulo="receita.titulo" :instrucoes="receita.instrucoes" :foto="transformarPath(receita.foto)")
        div.column.justify-center.botoes-editar.cursor-pointer
          div(@click="irPaginaEditarReceita(receita.id)").row.edit
            q-icon(name="mdi-pencil").q-mt-xs.icone-triangulo
            span Editar
          div(@click="deletarReceita(receita.id)").row
            q-icon(name="mdi-trash-can-outline").q-mt-xs.icone-triangulo
            span Excluir
</template>

<script>
import CardReceita from '../components/CardReceita.vue'
import { listAllRecipe, deleteRecipe } from '../services/recipe'
import { mapActions } from 'vuex'

export default {
  name: 'GerenciarReceitas',
  components: { CardReceita },
  data() {
    return {
      listaReceita: []
    }
  },
  methods: {
    ...mapActions('busca', ['setParametrosBusca']),
    mudarPagina() {
      this.$router.push({
        path: '/criarreceita'
      })
    },
    buscarReceitas() {
      listAllRecipe().then(({ data }) => {
        this.listaReceita = data
        this.triggerMensagem('positive', 'Todas receitas listadas.')
      }).catch((error) => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível obter a receitas')
      })
    },
    triggerMensagem(type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
      })
    },
    irPaginaEditarReceita(id){
      this.setParametrosBusca({
        id: id
      })
      const query = {
        id: id
      }
      const path = '/editarreceita'
      this.$router.push({ path, query })
    },
    deletarReceita(id){
      const idNumber = id
      deleteRecipe(idNumber).then(() => {
        this.triggerMensagem('positive', 'Receita deletada.')
        this.buscarReceitas()
      }).catch(error => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível deletar receita.')
      })
    },
    transformarPath(uploads) {
      const backendURL = 'http://localhost:5000'
      const nomeArquivo = uploads.substring(uploads.lastIndexOf('/') + 1)
      return `${backendURL}/images/${nomeArquivo}`
    }
  },
  mounted() {
    this.buscarReceitas()
  }
}
</script>
<style lang="sass" scoped>
.busca
  display: flex
  width: 100%

.edit
  margin-left: 15px
.btn
  margin: 15px
  width: 300px

.caixa-branca
  background-color: white
  border-radius: 20px
  padding: 10px
  align-items: center
  justify-content: center

.botoes-editar
  display: flex
  flex-direction: row-reverse
  justify-content: flex-start
</style>
