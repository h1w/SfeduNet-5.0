<template>
    <div style="margin-top: 1em !important;">
        <b-container >
        <div class="row justify-content-center">
            <div class="col-xs-12 col-sm-6 col-lg-8">
                <div class="page-my-account">
                    <div class="columns is-multiline">
                        <div class="column is-12">
                            <h1 class="title">Мой аккаунт</h1>
                        </div>

                        <div class="column is-12">
                            <button v-if="isLoggedIn" @click="logout()" class="button is-danger">Выйти</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </b-container>
    </div>
</template>

<script>
import axios from 'axios'
import { mapGetters, mapMutations } from "vuex";

export default {
    name: 'MyAccount',
    components: {
    },
    data() {
        return {

        }
    },
    computed: {
        ...mapGetters(["isLoggedIn"]),
    },
    mounted() {
        document.title = 'Мой аккаунт | Абмрозия'
    },
    methods: {
        ...mapMutations(["removeTokens"]),
        logout() {
            this.removeTokens()
            this.$router.push({ name: "map" });
            // axios.defaults.headers.common["Authorization"] = ""
            // localStorage.removeItem("token")
            // localStorage.removeItem("username")
            // localStorage.removeItem("userid")
            // this.$store.commit('removeToken')
            // this.$router.push('/')
        },
    }
}
</script>