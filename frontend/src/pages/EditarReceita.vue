<template lang="pug">
q-page
  section.q-pa-xl.column.pagina
    div.items-left
      li(@click="voltarPagina").row.secao-voltar
        q-icon(name="mdi-arrow-left-circle").q-mt-xs.icone-triangulo
        a.botao-voltar Voltar
    div.column
      span Título
      q-input(
        bg-color="white"
        v-model="aux.titulo"
        rounded
        color="grey"
        outlined
        borderless
        placeholder="Digite o título da receita"
      )
    div.row.checkbox
      div.column
        span Categorias
        div.caixa-branca.column
          q-radio(
            v-for="val in categorias"
            size="xs"
            v-model="aux.categorias[0]"
            :val="val"
            :label="value[val]"
            color="grey"
          )
      div.column 
        span Tags
        div.caixa-branca.column
          q-radio(
            v-for="val in tags"
            size="xs"
            v-model="aux.tags[0]"
            :val="val"
            :label="value[val]"
            color="grey"
          )
    div.column
      span Ingredientes:
      div(v-for="(ingrediente, index) in listaIngrediente")
        q-input(
          bg-color="white"
          v-model="listaIngrediente[index]"
          rounded
          color="grey"
          outlined
          borderless
          placeholder="Digite a porção e o ingrediente"
        ).q-pb-sm
      q-btn(rounded flat color="white" no-caps @click="addIngrediente").btn Adicionar Ingrediente
    div.column
      span Modo de Preparo:
      q-input(
        bg-color="white"
        v-model="aux.instrucoes"
        rounded
        color="grey"
        outlined
        borderless
        placeholder="Detalhe o modo de preparo"
        type="textarea"
      ).q-pb-md
    q-btn(rounded flat color="white" no-caps @click="cadastrarReceita").btn Salvar Receita 
</template>

<script>
import { editRecipe, searchById } from '../services/recipe'
import { mapGetters } from 'vuex'


export default {
  name: 'EditarReceita',
  components: {},
  data(){
    return{
      aux:{
        titulo: '',
        ingredientes: '',
        instrucoes: '',
        categorias: [],
        tags: [],
        files: []
      },
      listaIngrediente: [],
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
      ],
      value: {
        CAFE_DA_MANHA: 'Café da manhã',
        JANTAR: 'Jantar',
        ALMOCO: 'Almoço',
        DOCES: 'Doces',
        LANCHE: 'Lanche',
        LACTOSE: 'Lactose',
        OLEAGINOSAS: 'Oleaginosas',
        PORCO: 'Porco',
        CARNE: 'Carne',
        GLUTEN: 'Glúten',
        FRUTOSDOMAR: 'Frutos do mar'
      }
    }
  },
  computed:{
    ...mapGetters('busca', ['parametrosBusca'])
  },
  methods:{
    voltarPagina(){
      this.$router.push({
        path: '/administrador'
      })
    },
    addIngrediente(){
      this.listaIngrediente.push('')
    },
    addFoto(){
      this.aux.files.push('')
    },
    verificarReceita(){
      return 'receita'
    },
    cadastrarReceita(){
      let formData = new FormData()
      formData.append('titulo', this.aux.titulo)
      formData.append('ingredientes', this.transformarLista(this.listaIngrediente))
      formData.append('instrucoes', this.aux.instrucoes)
      formData.append('categorias', this.aux.categorias)
      formData.append('tags', this.aux.tags)

      console.log(formData)
      const idNumber = parseInt(this.parametrosBusca.id)
      editRecipe(
        idNumber,
        formData
        ).then(() => {
        this.triggerMensagem('positive', 'Receita cadastrada.')
        this.voltarPagina()
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
    },
    transformarLista(lista){
      return lista.join(',')
    },
    buscaReceitaPorId(){
      console.log(this.parametrosBusca.id)
      if(this.parametrosBusca.id != 0){
        searchById({
          receita_id: this.parametrosBusca.id
        }).then(({ data }) => {
          this.aux = data
          console.log(this.aux)
          this.triggerMensagem('positive', 'Receita encontrada.')
          this.loading = false
          this.transformToList() 
        }).catch(error => {
          console.log(error)
          this.triggerMensagem('negative', 'Não foi possível obter receita.')
        }) 
      }
    },
    transformToList() {
      if (!(this.aux.ingredientes === undefined)){ 
        if(this.aux.ingredientes[0].trim() === '') {
          
          this.listaIngrediente = []
        }else{
          const lista = this.aux.ingredientes[0].split(',')
  
          this.listaIngrediente = lista.map(item => item.trim())
        }
      }
    }
  },
  watch: {
    'parametrosBusca.id'() {
      this.buscaReceitaPorId()
    }
  },
  mounted() {
    this.buscaReceitaPorId()
  }
}
</script>
<style lang="sass" scoped>
.busca
  display: flex
  width: 100%

.btn
  margin: 15px
  width: 250px
  background-color: black
  text-color: white

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

.pagina
  gap: 20px

.caixa-branca
  background-color: white
  border-radius: 20px
  padding: 20px
  height: 250px
  width: 200px

.checkbox
  gap: 30px
</style>
