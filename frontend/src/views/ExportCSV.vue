<template>
    <div id="app">
    <div class="container">
        <div class="col-md-6">
          <h3>Vue Js Export as CSV Example - CodeCheef</h3>
          <download-csv
              :data = "json_data">
              Download Data
          </download-csv>
        </div>
    </div>
  </div>
</template>

<script>
import JsonCSV from 'vue-json-csv'

export default {
    name: 'ExportCSV',
    components: {
        'downloadCsv': JsonCSV
    },
    data() {
        return {
            json_data: [
                        {
                            'name': 'Tony Peña',
                            'city': 'New York',
                            'country': 'United States',
                            'birthdate': '1978-03-15',
                            'phone': {
                                'mobile': '1-541-754-3010',
                                'landline': '(541) 754-3010'
                            }
                        },
                        {
                            'name': 'Thessaloniki',
                            'city': 'Athens',
                            'country': 'Greece',
                            'birthdate': '1987-11-23',
                            'phone': {
                                'mobile': '+1 855 275 5071',
                                'landline': '(2741) 2621-244'
                            }
                        }
                    ],
            errors: [],
        }
    },
    mounted() {
        document.title = 'Выгрузка | Амброзия'
    },
    methods: {
    }
}
</script>