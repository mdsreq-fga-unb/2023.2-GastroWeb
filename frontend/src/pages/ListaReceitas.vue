<template lang="pug">
q-page
  section.q-pa-xl.column
    li(@click="voltarPagina").row.secao-voltar
      q-icon(name="mdi-arrow-left-circle").q-mt-xs.icone-triangulo
      a.botao-voltar Voltar
    q-spinner-oval(
      v-if="loading"
      color="grey"
      size="3em"
    )
    div(v-else)
      span Receitas:
      div(v-for="(receita, index) in listaReceita")
        span {{receita?.titulo}}
    CardReceita
</template>

<script>
import CardReceita from '../components/CardReceita.vue'
import { searchByName } from '../services/recipe'
import { mapGetters } from 'vuex'

export default {
  name: 'ListaReceitas',
  components: { CardReceita },
  data(){
    return{
      listaReceita: [],
      loading: true
    }
  },
  computed: {
    ...mapGetters('busca', ['parametrosBusca'])
  },
  methods:{
    voltarPagina(){
      this.$router.push({
        path: '/'
      })
    },
    obterReceitas(){
      console.log(this.parametrosBusca.titulo)
      searchByName({
        titulo: this.parametrosBusca.titulo
      }).then(({ data }) => {
        this.listaReceita = data
        this.triggerMensagem('positive', 'Receitas encontradas.')
        this.loading = false
      }).catch(error => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível cadastrar receita.')
      })
    },
    triggerMensagem (type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
      })
    }
  },
  watch: {
    'parametrosBusca.titulo'() {
      this.obterReceitas()
    }
  },
  mounted(){
    this.obterReceitas()
  }
}
</script>
<style lang="sass">
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
