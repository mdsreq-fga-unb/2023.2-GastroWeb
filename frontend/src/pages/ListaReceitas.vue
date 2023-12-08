<template lang="pug">
q-page
  section.q-pa-xl.column
    li(@click="voltarPagina").row.secao-voltar
      q-icon(name="mdi-arrow-left-circle").q-mt-xs.icone-triangulo
      a.botao-voltar Voltar
    //- q-spinner-oval(
    //-   v-if="loading"
    //-   color="grey"
    //-   size="3em"
    //- )
    div
      span Receitas:
      div(v-for="(receita, index) in listaReceita")
        CardReceita(:id="receita.id" :titulo="receita.titulo" :instrucoes="receita.instrucoes" :foto="foto" @click="irParaReceita(receita.id)")
</template>

<script>
import CardReceita from '../components/CardReceita.vue'
import { searchByName } from '../services/recipe'
import { mapGetters } from 'vuex'

export default {
  name: 'ListaReceitas',
  components: { CardReceita },
  data() {
    return {
      listaReceita: [
        {
          titulo: 'macarrao com salsicha',
          id: 1,
          instrucoes: 'salsicha cozida'
        },
        {
          titulo: 'bolo de fuba',
          id: 2,
          instrucoes: 'mistura tudo'
        },
        {
          titulo: 'bolo de canoura',
          id: 3,
          instrucoes: 'corte tudo'
        },
        {
          titulo: 'aaaaaaa',
          id: 4,
          instrucoes: 'aaaaaaaaaaa'
        },
        {
          titulo: 'feijoada do RU',
          id: 5,
          instrucoes: 'aprenda a fazer feijão'
        },
        {
          titulo: 'ssssssss',
          id: 6,
          instrucoes: 'sssssssss'
        },
        {
          titulo: 'pernil',
          id: 7,
          instrucoes: 'aaaaaaaaaaaaaa'
        },
        {
          titulo: 'aaaaaaaaa',
          id: 8,
          instrucoes: 'aaaaaaaaaa'
        },
        {
          titulo: 'camarao mediterraneo',
          id: 9,
          instrucoes: 'aaaaaadddddddddd'
        },
        {
          titulo: 'arroz negro',
          id: 10,
          instrucoes: 'fffffffffffffffffffff'
        },
        {
          titulo: 'penne ao funghi',
          id: 12,
          instrucoes: 'fffffffffffffff'
        },
        {
          titulo: 'parmegiana',
          id: 13,
          instrucoes: 'empane e frite'
        },
        {
          titulo: 'salmao na bananeira',
          id: 14,
          instrucoes: 'assa esses trem'
        }
      ],
      loading: false,
      foto: 'uploads/testeunb.jpeg'
    }
  },
  computed: {
    ...mapGetters('busca', ['parametrosBusca'])
  },
  methods: {
    voltarPagina() {
      this.$router.push({
        path: '/'
      })
    },
    obterReceitas() {
      console.log(this.parametrosBusca.titulo)
      // searchByName({
      //   titulo: this.parametrosBusca.titulo
      // }).then(({ data }) => {
      //   this.listaReceita = data
      //   this.triggerMensagem('positive', 'Receitas encontradas.')
      //   this.loading = false
      // }).catch(error => {
      //   console.log(error)
      //   this.triggerMensagem('negative', 'Não foi possível cadastrar receita.')
      // })
      
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
    }
  },
  watch: {
    'parametrosBusca.titulo'() {
      this.obterReceitas()
    }
  },
  mounted() {
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
