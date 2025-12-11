import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, Image, TouchableOpacity, ScrollView,  } from 'react-native';
import { useRouter } from 'expo-router';
import {
  SafeAreaView,
  SafeAreaProvider,
} from 'react-native-safe-area-context';




export default function App() {
    const router = useRouter();
    const [saleVisible, setSale] = useState(false)


    return (
      <>
          <SafeAreaProvider>
            <SafeAreaView style={{ flex:1,  backgroundColor:'#fff'}}>
              <StatusBar  barStyle='dark-content' translucent/>
              <ScrollView>
              {/* header */}
              <View style={{
                backgroundColor:'#8A19D6',
                alignItems: 'center',
                justifyContent: 'center',
                height:178,
              }}>
                <View style={styles.cabecalho}>
                  <View style={styles.boxIconesCabecalho}>
                    <View style={styles.circulo}>
                        <Image style={styles.icone} source={require('./img/user.png')} />
                    </View>

                    <View style={styles.itensIcones} >
                      <TouchableOpacity onPress={ () => { setSale(!saleVisible) }}>
                        { saleVisible ? 
                          <Image style={styles.icone} source={require('./img/eye.png')} /> 
                          :
                          <Image style={styles.icone} source={require('./img/olho.png')} />
                        }
                      </TouchableOpacity>
                      <View>
                      <Image style={styles.icone} source={require('./img/ajuda.png')} />
                      </View>
                      <View>
                      <Image style={styles.icone} source={require('./img/email.png')} />
                      </View>
                    </View>
                  </View>

                  <View style={styles.boxTextUsuario}>
                    <Text style={styles.textUsuario}>Olá, Gabriela</Text>
                  </View>
                </View>
                <View>
                </View>
              </View>

              {/* Section */}
              <View style={stylesSection.container}>
                  <View style={stylesSection.content}>
                    <Text style={stylesSection.title}>Conta</Text>
                    
                    { saleVisible ? 
                      <Text style={stylesSection.titleSaldo}>R$40.221,00</Text>
                      :
                      <View  style={{ backgroundColor: '#ccc', width:150, borderRadius: 8, opacity:0.2}}>
                        <Text style={stylesSection.titleSaldo}></Text>
                      </View>
                    }
                    
                   
                    <ScrollView  
                      horizontal 
                      showsHorizontalScrollIndicator={false} 
                      contentContainerStyle={stylesSection.containerScrol}
                    >
                      <View style={stylesSection.contentOptions} >
                        <TouchableOpacity onPress={() => router.navigate('/sobre')} style={stylesSection.circuloOptions}>
                          <Image  source={require('./img/Index/options/pix.png')} />
                        </TouchableOpacity>
                        <Text style={stylesSection.titleOptions}>Área Pix</Text>
                      </View>

                      <View style={stylesSection.contentOptions} >
                        <TouchableOpacity style={stylesSection.circuloOptions}>
                          <Image  source={require('./img/Index/options/cod_barras.png')} />
                        </TouchableOpacity>
                        <Text style={stylesSection.titleOptions}>Pagar</Text>
                      </View>

                      <View style={stylesSection.contentOptions} >
                        <TouchableOpacity style={stylesSection.circuloOptions}>
                          <Image  source={require('./img/Index/options/transferir.png')} />
                        </TouchableOpacity>
                        <Text style={stylesSection.titleOptions}>Transferir</Text>
                      </View>
                      
                      <View style={stylesSection.contentOptions} >
                        <TouchableOpacity style={stylesSection.circuloOptions}>
                          <Image  source={require('./img/Index/options/depositar.png')} />
                        </TouchableOpacity>
                        <Text style={stylesSection.titleOptions}>Depositar</Text>
                      </View> 
                      
                      <View style={stylesSection.contentOptions} >
                        <TouchableOpacity style={stylesSection.circuloOptions}>
                          <Image  source={require('./img/Index/options/recarga.png')} />
                        </TouchableOpacity>
                        <Text style={stylesSection.titleOptions}>Recarga</Text>
                      </View>
                    </ScrollView>

                  
                    <View style={stylesSection.cartoes}>
                      <Image source={require('./img/Index/cartoes.png')} /> 
                      <Text style={{ fontWeight: 500}}>Meus Cartões</Text>
                    </View>

                    <ScrollView 
                      horizontal 
                      showsHorizontalScrollIndicator={false} 
                      contentContainerStyle={stylesSection.containerScrol}
                    >
                      <View style={ {flexDirection: 'row',  gap:12, flex:1, marginTop:-20}}>
                        <View style={stylesSection.inforRend}>
                          <Text style={{ fontWeight: 500 }}>Seu <Text style={{ color:'#8A19D6' }}>informe de rendimentos</Text> 2021 já está disponível</Text>
                        </View>
                        
                        <View style={stylesSection.inforRend}>
                          <Text style={{ fontWeight: 500 }}>Seu <Text style={{ color:'#8A19D6' }}>informe de rendimentos</Text> 2021 já está disponível</Text>
                        </View>
                      </View>

                    </ScrollView>
                   
                </View>
              </View>

              {/* Cartao */}
              <View style={stylesGeneric.hr}/>
              <View style={stylesCartao.container}>
                <View style={stylesCartao.content}>
                  <Image style={{ marginTop:20 }}source={require('./img/Index/cartoes.png')} /> 
                  <Text style={stylesSection.title}>Cartão de crédito</Text>
                  
                  <Text style={{ fontWeight: 500 , marginTop:20, marginBottom:20 }}>Peca seu cartão de crédito sem anuidade e tenha mais controle da sua vida financeira.</Text>

                  <TouchableOpacity id='pedircartao' style={stylesGeneric.button}>
                    <Text style={stylesGeneric.buttonText}>Pedir Cartão</Text>
                  </TouchableOpacity>
                </View>
              </View>

              {/* Portabilidade */}
              <View style={stylesGeneric.hr}/>
              <View style={stylesPortabilidade.container}>
                <View style={stylesPortabilidade.content}>
                  <Text style={{ fontWeight: 700, fontSize:18, marginBottom:15}}>Descubra mais</Text>
                    <ScrollView 
                      horizontal 
                      showsHorizontalScrollIndicator={false} 
                      contentContainerStyle={stylesPortabilidade.containerScrol}
                    >

                      <View style={stylesPortabilidade.carPort} >
                        <Image source={require('./img/Index/portabilidade.png')} /> 
                        <View style={{ padding:16, gap:8}}>
                          <Text style={{ fontWeight: 500, fontSize:16}}>Portabilidade de salário</Text>
                          <Text style={{ fontWeight: 300, color:'#000000'}}>Sua liberdade financeira comeca com você escolhendo...</Text>

                          <TouchableOpacity id='conhecer1' style={stylesGeneric.button}>
                            <Text style={stylesGeneric.buttonText}>Conhecer</Text>
                          </TouchableOpacity>
                        </View>
                      </View>
                      <View style={stylesPortabilidade.carPort} >
                        <Image source={require('./img/Index/portabilidade.png')} /> 
                        <View style={{ padding:16, gap:8}}>
                          <Text style={{ fontWeight: 500, fontSize:16}}>Portabilidade de salário</Text>
                          <Text style={{ fontWeight: 300, color:'#000000'}}>Sua liberdade financeira comeca com você escolhendo...</Text>

                          <TouchableOpacity id='conhecer2' style={stylesGeneric.button}>
                            <Text style={stylesGeneric.buttonText}>Conhecer</Text>
                          </TouchableOpacity>
                        </View>
                      </View>
                    </ScrollView>
                </View>
              </View>

              </ScrollView>
            </SafeAreaView>
          </SafeAreaProvider>
      </>
  );
}

const styles = StyleSheet.create({
  container:{
    height:'auto',
    alignItems: 'center',
    backgroundColor: '#fff', 
  },

  cabecalho:{
    flex:1,
    backgroundColor: '#8A19D6',
    width: '100%',
    height: 178,
    paddingHorizontal: 20,
  },

  icone:{
    width: 20,
    height:20
  },

  circulo:{
    width: 40,
    height: 40,
    backgroundColor: '#9603E8',
    borderRadius: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },


  boxIconesCabecalho: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 53
  },


  itensIcones:{
    flexDirection:'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    gap: 15,
  },

  boxTextUsuario:{
    marginTop: 20
  },

  textUsuario:{
    color: 'white',
    fontSize: 15,
    fontWeight: 'bold',
  }
})

const stylesSection = StyleSheet.create({
  container:{
    flex:1,
    height:'100%',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 20
  },
  
  content:{
    backgroundColor: '#fff',
    width: '100%',
    paddingHorizontal: 20,
  },
  
  title:{
    marginTop:20,
    fontSize:22,
    fontWeight: 500
  },
  
  titleOptions:{
    fontSize:14,
    fontWeight: 500
  },

  titleSaldo:{
    fontSize:26,
    fontWeight: 700
  },

  ocult:{
    backgroundColor:'#ccc',
    width:150,
  },

  containerScrol: {
    marginTop:40,
  },

  contentOptions:{
    alignItems:'center',
    paddingHorizontal: 7,
  },

  circuloOptions:{
    width: 63,
    height: 63,
    marginLeft: 0, 
    backgroundColor: '#f0f1f5',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 100,
  },


  cartoes:{
    backgroundColor: '#f0f1f5',

    flexDirection: 'row',
    gap: 10,
    marginTop:20,
    width:'100%',
    height: 56,
    borderRadius: 12,

    padding:16
  },
  
  inforRend:{
    backgroundColor: '#f0f1f5',
    
    width: 263,
    height: 80,
    borderRadius: 12,

    paddingTop:16,
    paddingLeft:16,
    paddingRight:16,
    paddingBottom:10

  },



})

const stylesCartao = StyleSheet.create({
  container:{
    flex:1,
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom:20
  },
  
  content:{
    backgroundColor: '#fff',
    width: '100%',
    paddingHorizontal: 20,
  }

})

const stylesPortabilidade = StyleSheet.create({
  container:{
    flex:1,
    alignItems: 'center',
    justifyContent: 'space-between',
    marginTop:20,
    marginBottom:20,
  },
  
  content:{
    backgroundColor: '#fff',
    width: '100%',
    paddingHorizontal: 20,
  },

  carPort:{
    backgroundColor:'#F0F1F5',
    borderRadius:10,
    width: 236,
    height: 272,
    gap: 10,
  },

  containerScrol:{
    gap:19
  }


})

const stylesGeneric = StyleSheet.create({
  button:{
    backgroundColor:'#8A19D6',
    alignItems:'center',
    width: 139,
    height: 46,
    gap: 10,
    borderRadius: 23,
    paddingTop: 12,
    paddingRight: 24,
    paddingBottom: 12,
    paddingLeft: 24,
  },

  buttonText:{
    color:'#fff',
    fontWeight:700
  },

  hr: {
    borderBottomColor: '#F0F1F5',
    borderBottomWidth: 1,          
  },

})