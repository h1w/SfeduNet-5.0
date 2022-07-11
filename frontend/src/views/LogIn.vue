<template>
    <div style="margin-top: 1em !important;">
            <b-container >
            <div class="row justify-content-center">
                <div class="col-xs-12 col-sm-6 col-lg-8">
                    <div class="page-log-in">
                        <div class="columns">
                            <div class="column is-4 is-offset-4">
                                <h1 class="title text-center">Войти</h1>
                                <div class="row justify-content-center">
                                    <b-form @submit="submitForm">
                                        <!-- <div class="field">
                                            <label>Логин</label>
                                            <div class="control">
                                                <input type="text" class="input" v-model="username">
                                            </div>
                                        </div> -->
                                        
                                        <!-- <div class="field">
                                            <label>Пароль</label>
                                            <div class="control">
                                                <input type="password" class="input" v-model="password">
                                            </div>
                                        </div>
                                        <br> -->

                                        <b-form-input
                                        id="input-1"
                                        v-model="form.username"
                                        required
                                        placeholder="Введите логин"
                                        ></b-form-input>

                                        <b-form-input
                                        id="input-2"
                                        type="password"
                                        v-model="form.password"
                                        required
                                        placeholder="Введите пароль"
                                        class="mt-3"
                                        ></b-form-input>

                                        <div class="mt-2">
                                            <b-button variant="outline-success" class="button is-dark" @click="submitForm()">Войти</b-button>
                                        </div>

                                        <!-- <div class="notification is-danger" v-if="errors.length">
                                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                        </div>

                                        <div class="field">
                                            <div class="control">
                                                <b-button variant="outline-success" class="button is-dark">Войти</b-button>
                                            </div>
                                        </div> -->

                                        <hr>
                                    </b-form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </b-container>
    </div>
</template>

<style scoped>
</style>

<script>
import axios from 'axios'
import { mapMutations } from "vuex";

export default {
    name: 'LogIn',
    data() {
        return {
            form: {
                username: '',
                password: '',
                errors: []
            },
        }
    },
    mounted() {
        document.title = 'Вход | Амброзия'
    },
    methods: {
        ...mapMutations(["setTokens"]),
        async submitForm() {
            const formData = {
                username: this.form.username,
                password: this.form.password
            }
            await axios
                .post("/api/v1/auth/jwt/create/", formData, {
                    headers: {
                        "Content-Type": "application/json",
                    }
                })
                .then(response => {
                    var accessToken = response.data.access
                    var refreshToken = response.data.refresh
                    
                    this.setTokens(accessToken, refreshToken)

                    this.$router.push({ name: "map" });
                })
                .catch(error => {
                    this.form.errors = []
                    if (error.response) {
                        console.log(JSON.stringify(error))
                        for (const property in error.response.data) {
                            this.form.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    }
                })
        }

        // ...mapMutations(["setTokens"]),
        // async submitForm() {
        //     const formData = {
        //         username: this.username,
        //         password: this.password
        //     }
        //     await axios
        //         .post("/api/v1/auth/jwt/create", formData, {
        //             headers: {
        //                 "Content-Type": "application/json",
        //             }
        //         })
        //         .then(response => {
        //             accessToken = response.data.access
        //             refreshToken = response.data.refresh
        //             this.setTokens(accessToken, refreshToken);
        //         })
        //         .catch(error => {
        //             console.log(JSON.stringify(error))
        //         })

            // axios.defaults.headers.common["Authorization"] = ""
            // localStorage.removeItem("token")
            // const formData = {
            //     username: this.username,
            //     password: this.password
            // }
            // await axios
            //     .post("/api/v1/auth/jwt/create/", formData)
            //     .then(response => {
            //         this.$store.commit("updateToken", response.data.access);
                    
            //         // get and set auth user
            //         this.$store.commit("setAuthUser", {
            //             authUser: response.data,
            //             isAuthenticated: true,
            //         });
            //         // this.$router.push({ name: "map" });

            //         // const token = response.data.access
            //         // const refreshToken = response.data.refresh
            //         // this.$store.commit('setToken', token, refreshToken)
                    
            //         // axios.defaults.headers.common["Authorization"] = "Bearer " + token
            //         // localStorage.setItem("token", token)
            //         const toPath = this.$route.query.to || '/'
            //         this.$router.push(toPath)
            //     })
            //     .catch(error => {
            //         if (error.response) {
            //             for (const property in error.response.data) {
            //                 this.errors.push(`${property}: ${error.response.data[property]}`)
            //             }
            //         } else {
            //             this.errors.push('Something went wrong. Please try again')
                        
            //             console.log(JSON.stringify(error))
            //         }
            //     })
        // }
    }
}
</script>