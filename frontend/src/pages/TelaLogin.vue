<template>
    <div class="container">
        <div class="row">
            <div class="sidePhoto">
                <img id="loginImage" src="../assets/loginImage.png" alt="loginImage">
            </div>
            <div class="card">
                <div class="formulario">
                    <img id="logoImage" src="../assets/logoBlack.png" alt="logoImage">

                    <div class="conteudo">
                        <div class="textCard">
                            <p id="title">Bem-vinda</p>
                            <p id="logintext">Faça seu login</p>
                        </div>

                        <!-- <form action=""> -->
                        <input type="text" placeholder="usuário" v-model="info.usuario">
                        <input type="password" placeholder="senha" v-model="info.senha">

                        <button @click="fazerLogin" class="btn-dark">Entrar</button>
                        <!-- </form> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { login } from '../services/login'
import { mapActions } from 'vuex'


export default {
  name: 'TelaLogin',
  components: {},
  data() {
    return{
      info: {
        usuario: '',
        senha: ''
      }
    }
  },
  methods: {
    ...mapActions('login', ['setLogin', 'setLoading']),
    fazerLogin(){
      const dados = new URLSearchParams()
      dados.append('grant_type', '')
      dados.append('username', this.info.usuario)
      dados.append('password', this.info.senha)
      dados.append('scope', '')
      dados.append('client_id', '')
      dados.append('client_secret', '')
      login(dados).then(async (data) => {
        this.setLogin(true)
        await this.sleep(1000)
        this.triggerMensagem('positive', 'Login realizado.')
        localStorage.setItem('token', data.token_type)
        this.$router.push({
          path: '/administrador'
        })
      }).catch(error => {
        console.log(error)
        this.triggerMensagem('negative', 'Erro ao fazer login.')
      })
    },
    triggerMensagem(type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
      })
    },
    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms))
    }
  }
}
</script>
<style scoped>
.row {
    display: flex;
    justify-content: center;
}

.card {
    background-color: white;
    width: 326px;
    border-radius: 0px 18px 18px 0px;
    height: 450px;
}

.formulario {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.conteudo {
    align-items: center;
    display: flex;
    flex-direction: column;
}

.textCard {
    margin-top: 20px;
}

form {
    display: flex;
    flex-wrap: center;
    flex-direction: column;
    margin-top: 10px;
}

input {
    margin-bottom: 5px;
    width: 225px;
    height: 45px;
    border-radius: 8px;
    background: #F0EFDD;
    text-align: center;
    border: 0;
}

p {
    margin: 9px;
}

.btn-dark {
    color: #fff;
    background-color: #343a40;
    border-color: #343a40;
    border-radius: 25px;
    height: 45px;
    width: 130px;
    margin-top: 10px;
}

.btn-dark:hover {
    color: #fff;
    background-color: #23272b;
    border-color: #1d2124;
}

.btn-dark:focus,
.btn-dark.focus {
    color: #fff;
    background-color: #23272b;
    border-color: #1d2124;
    box-shadow: 0 0 0 0.2rem rgba(52, 58, 64, 0.5);
}

.btn-dark.disabled,
.btn-dark:disabled {
    color: #fff;
    background-color: #343a40;
    border-color: #343a40;
}

.btn-dark:not(:disabled):not(.disabled):active,
.btn-dark:not(:disabled):not(.disabled).active,
.show>.btn-dark.dropdown-toggle {
    color: #fff;
    background-color: #1d2124;
    border-color: #171a1d;
}

.btn-dark:not(:disabled):not(.disabled):active:focus,
.btn-dark:not(:disabled):not(.disabled).active:focus,
.show>.btn-dark.dropdown-toggle:focus {
    box-shadow: 0 0 0 0.2rem rgba(52, 58, 64, 0.5);
}

#loginImage {
    height: 450px;
}

#logoImage {
    height: 46px;
    margin-top: 60px;
}

#title {
    font-size: 32px;
    font-style: normal;
    font-weight: 700;
    font-size: 32px;
    margin-bottom: 5px;
}

#logintext {
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
}

/* Estilos para dispositivos menores, como tablets e smartphones */
@media screen and (max-width: 768px) {
    .card {
        width: 100%;
        /* Ocupar a largura total */
        border-radius: 18px;
        /* Ajuste do raio */
        margin: 10px;
        /* Espaçamento entre os cards */
    }

    #loginImage {
        height: auto;
        /* Ajuste da altura da imagem */
        width: 100%;
        /* Ocupar a largura total */
    }

    #logoImage {
        height: 30px;
        /* Tamanho do logo para telas menores */
        margin-top: 30px;
        /* Ajuste do espaçamento do logo */
    }

    #title {
        font-size: 24px;
        /* Tamanho do título para telas menores */
        margin-bottom: 5px;
    }

    #logintext {
        font-size: 18px;
        /* Tamanho do texto de login para telas menores */
    }

    input {
        width: 100%;
        /* Ocupar a largura total */
    }
}
</style>
    