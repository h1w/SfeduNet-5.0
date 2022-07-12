<template>
    <b-container class="page-log-in" style="margin-top: 1em !important;">
        <b-row class="align-items-center" align-v="center">
            <b-col class="align-self-center">
                <b-container class="jumbotron d-flex align-items-center" id="login-form-container">
                    <div class="container">
                        <p id="login-title-text" class="text-center">Авторизация</p>
                        
                        <br>

                        <div class="row justify-content-center">
                            <b-form @submit="submitForm" class="mt-1" style="width: 20rem;">
                                <b-form-group
                                    id="input-group-1"
                                    label="Логин"
                                    label-for="input-1-password-loginform"
                                    description=""
                                >
                                    <b-form-input
                                    id="input-1-password-loginform"
                                    v-model="form.username"
                                    required
                                    placeholder="Логин"
                                    ></b-form-input>
                                </b-form-group>    

                                <b-form-group
                                    id="input-group-2"
                                    label="Пароль"
                                    label-for="input-2-password-loginform"
                                    description=""
                                >
                                    <b-form-input
                                    id="input-2-password-loginform"
                                    type="password"
                                    v-model="form.password"
                                    required
                                    placeholder="..."
                                    class="mt-3"
                                    ></b-form-input>
                                </b-form-group>

                                <br>
                                
                                <b-button id="login-button" variant="success" class="button is-dark" @click="submitForm()">Войти</b-button>
                            </b-form>
                        </div>
                    </div>    
                </b-container>
            </b-col>
        </b-row>
    </b-container>
    <!-- <div style="margin-top: 1em !important;">
        <div class="page-log-in">
            
        </div>
    </div> -->
</template>

<style scoped>
#login-form-container {
    /* height:100%;
    width:100%;

    text-align: center; */

    background-color: #FFFFFF;
}

#login-form-container > .container {
    /* max-width: 100%;
    
    display: inline-block;
    vertical-align: middle; */
}

#login-title-text {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 30px;
    line-height: 120%;
    /* identical to box height, or 36px */

    text-transform: uppercase;

    color: #000000;
}

#login-button {
    width: 100%;
    background: #95E375 !important;
    border-radius: 24px !important;
    border-color: #95E375;
    height: 3em;

    font-family: 'Nunito' !important;
    font-style: normal !important;
    font-weight: 800 !important;
    font-size: 15px !important;
    line-height: 120% !important;
    /* or 18px */

    text-transform: uppercase;

    color: #FFFFFF;
}
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