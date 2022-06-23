<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Войти</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Логин</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Войти</button>
                        </div>
                    </div>

                    <hr>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Вход | Амброзия'
    },
    methods: {
        async submitForm() {
            const formData = {
                username: this.username,
                password: this.password
            }
            await this.$store.commit("userLogin", formData)
            this.$router.push({ name: 'map' })

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
        }
    }
}
</script>