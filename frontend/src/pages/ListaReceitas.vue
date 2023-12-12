<template lang="pug">
q-page
  section.q-pa-xl.column
    li(@click="voltarPagina").row.secao-voltar
      q-icon(name="mdi-arrow-left-circle").q-mt-xs.icone-triangulo
      a.botao-voltar Voltar
    div(v-if="listaReceita.length > 0")
      h4 Receitas:
      div(v-for="(receita, index) in listaReceita")
        CardReceita(
          :id="receita.id"
          :titulo="receita.titulo"
          :instrucoes="receita.instrucoes"
          :foto="transformarPath(receita.fotos)"
          @click="irParaReceita(receita.id)"
        ).cursor-pointer
    div(v-else).justify-center.row
      h4 Nenhuma receita encontrada
</template>

<script>
import CardReceita from '../components/CardReceita.vue'
import { searchByName, searchByTagCategory } from '../services/recipe'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ListaReceitas',
  components: { CardReceita },
  data() {
    return {
      listaReceita: [],
      loading: false
    }
  },
  computed: {
    ...mapGetters('busca', ['parametrosBusca'])
  },
  methods: {
    ...mapActions('busca', ['setParametrosBusca']),
    voltarPagina() {
      this.$router.push({
        path: '/'
      })
    },
    obterReceitasPorTitulo() {
      console.log(this.parametrosBusca.titulo)
      if(this.parametrosBusca.titulo){
        searchByName({
          titulo: this.parametrosBusca.titulo
        }).then(({ data }) => {
          this.listaReceita = data[1]
          this.triggerMensagem('positive', 'Receitas encontradas.')
          this.loading = false
        }).catch(error => {
          console.log(error)
          this.triggerMensagem('negative', 'Não foi possível obter receitas.')
        }) 
      }
    },
    obterReceitasPorTagCategoria() {
      console.log(this.parametrosBusca.tags)
      console.log(this.parametrosBusca.categorias)
      searchByTagCategory({
        categoria: this.transformarLista(this.parametrosBusca.categorias),
        tag: this.transformarLista(this.parametrosBusca.tags)
      }).then(({ data }) => {
        this.listaReceita = data[1]
        this.triggerMensagem('positive', 'Receitas encontradas.')
        this.loading = false
      }).catch(error => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível obter receitas.')
      }) 
    },
    transformarLista(lista){
      return lista.join(',')
    },
    triggerMensagem(type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
      })
    },
    irParaReceita(id) {
      const query = {
        id: id
      }
      const path = '/exibirreceita'
      this.$router.push({ path, query })
      this.setParametrosBusca({
        ...this.parametrosBusca,
        id: id
      })
    },
    transformarPath(uploads) {
      const backendURL = 'http://localhost:3000'
      const nomeArquivo = uploads.substring(uploads.lastIndexOf('/') + 1)

      return `${backendURL}/images/${nomeArquivo}`
    }
  },
  watch: {
    'parametrosBusca.titulo'() {
      this.obterReceitasPorTitulo()
    },
    'parametrosBusca.tags'() {
      this.obterReceitasPorTagCategoria()
    },
    'parametrosBusca.categorias'() {
      this.obterReceitasPorTagCategoria()
    }
  },
  mounted() {
    if(!(this.parametrosBusca.titulo === '' || this.parametrosBusca.titulo === undefined)){
      this.obterReceitasPorTitulo()
    }else if (this.parametrosBusca.tags.length > 0 || this.parametrosBusca.categorias.length > 0){
      this.obterReceitasPorTagCategoria()
    }
  }
}
</script>
<style lang="sass" scoped>
.secao-voltar
  gap: 5px
  cursor: pointer

.botao-voltar
  font-weight: 700
  color: white
  font-size: 15px
  line-hegiht: 18px
  height: 20px
  text-decoration: none

.icone-triangulo
    color: white
    size: 50px

</style>