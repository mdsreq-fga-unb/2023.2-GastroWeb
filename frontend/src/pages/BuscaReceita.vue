<template lang="pug">
q-page
  section.q-pa-xl.column
    div(v-if="!buscaCheckbox").column.caixa-branca
      q-input(
        bg-color="white"
        rounded
        color="grey"
        outlined
        borderless
        placeholder="Pesquise uma receita"
        v-model="busca.titulo"
        @keyup.enter="buscarPorTitulo"
      ).busca
      q-btn(@click="buscarPorTitulo" color="black" text-color="white" no-caps :disable="busca.titulo === ''").btn Buscar
    div(v-else).column.caixa-branca
      div.row.checkbox
        div.column
          span Categorias
          q-checkbox(
            v-for="val in categorias"
            size="xs"
            v-model="selecionados.categorias"
            :val="val"
            :label="val"
          )
        div.column 
          span Tags
          q-checkbox(
            v-for="val in tags"
            size="xs"
            v-model="selecionados.tags"
            :val="val"
            :label="val"
          )
      q-btn(@click="buscarPorTagsCategorias" color="black" text-color="white" no-caps :disable="!(selecionados.tags.length > 0 ||  selecionados.categorias.length > 0)").btn Buscar
    div.q-pt-lg 
      span(v-if="!buscaCheckbox" @click="buscaCheckbox=!buscaCheckbox").cursor-pointer Pesquisa por Tag e Categoria
      span(v-else @click="buscaCheckbox=!buscaCheckbox").cursor-pointer Pesquisa por Título
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'BuscaReceita',
  components: {},
  data(){
    return{
      busca: {
        titulo: ''
      },
      buscaCheckbox: false,
      selecionados: {
        tags: [],
        categorias: []
      },
      tags: [
        'LACTOSE',
        'OLEAGINOSAS',
        'PORCO',
        'CARNE',
        'GLUTEN',
        'FRUTOSDOMAR'
      ],
      categorias: [
        'CAFE_DA_MANHA',
        'JANTAR',
        'ALMOCO',
        'DOCES',
        'LANCHE'
      ]
    }
  },
  methods:{
    ...mapActions('busca', ['setParametrosBusca']),
    ...mapActions('login', ['setLogin']),
    buscarPorTitulo(){
      this.setParametrosBusca({
        titulo: this.busca.titulo || ''
      })
      const query = {
        titulo: this.busca.titulo
      }
      const path = '/receitas'
      this.$router.push({ path, query })
    },
    buscarPorTagsCategorias(){
      this.setParametrosBusca({
        tags: this.arrayfy(this.selecionados.tags),
        categorias: this.arrayfy(this.selecionados.categorias)
      })
      const query = {
        tags: this.selecionados.tags,
        categorias: this.selecionados.categorias
      }
      const path = '/receitas'
      this.$router.push({ path, query })
    },
    arrayfy (data) {
      return data
        ? Array.isArray(data)
          ? data
          : [ data ]
        : []
    }
  },
  mounted(){
    this.setParametrosBusca({
      titulo: '',
      tags: [],
      categorias: [],
      id: 0
    }),
    this.setLogin(false)
    localStorage.removeItem('token')

  }
}
</script>
<style lang="sass" scoped>
.busca
  display: flex
  width: 100%

.btn
  margin: 15px
  width: 200px
  

.checkbox
  gap: 100px
  justify-content: center

.caixa-branca
  background-color: white
  border-radius: 20px
  padding: 20px
  height: 310px
  align-items: center
  justify-content: center
</style>
