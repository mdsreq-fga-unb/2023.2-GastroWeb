<template lang="pug">
q-page
  section.q-pa-xl.column
    span Página de Administrador
    q-btn(@click="mudarPagina" color="white" text-color="black").btn Criar Receita
    div(v-for="(receita, index) in listaReceita")
      CardReceita(:id="receita.id" :titulo="receita.titulo" :instrucoes="receita.instrucoes" :foto="foto" @click="irParaReceita(receita.id)")

    
</template>

<script>
import CardReceita from '../components/CardReceita.vue'
import { listAllRecipe } from '../services/recipe'

export default {
  name: 'GerenciarReceitas',
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
      foto: 'uploads/testeunb.jpeg'
    }
  },
  methods: {
    mudarPagina() {
      this.$router.push({
        path: '/criarreceita'
      })
    },
    buscarReceitas() {
      listAllRecipe().then(({ data }) => {
        this.listaReceita = data
        // this.loading = false
      }).catch((error) => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível obter a receitas')
        // this.loading = true
      })
    },
    triggerMensagem(type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
      })
    }
  },
  mounted() {
    this.buscarReceitas()
  }
}
</script>
<style lang="sass">
.busca
  display: flex
  width: 100%

.btn
  margin: 15px
</style>
