import { StatusBar } from "expo-status-bar"
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableOpacity,
  ScrollView,
  TextInput,
} from "react-native"
import { useRouter } from "expo-router"
import { SafeAreaView, SafeAreaProvider } from "react-native-safe-area-context"

const LinhaDivisoria = () => {
  return <View style={styles.linha} />
}

export default function Tela_procura_pix() {
  const router = useRouter()

  return (
    <>
      <SafeAreaProvider>
        <SafeAreaView style={{ flex: 1, backgroundColor: "#fff" }}>
          <StatusBar barStyle="dark-content" translucent />
          <ScrollView>
            {/* header */}
            <View
              style={{
                backgroundColor: "#8A19D6",
                alignItems: "center",
                justifyContent: "center",
                height: 178,
              }}
            >
              <View style={styles.cabecalho}>
                <View style={styles.boxIconesCabecalho}>
                  <View>
                    <TouchableOpacity onPress={() => router.back()}>
                      <Image
                        style={styles.icone}
                        source={require("./img/seta-esquerda.png")}
                      />
                    </TouchableOpacity>
                  </View>

                  <View style={{ gap: 15 }}>
                    <Text style={styles.textTitle}>
                      Para quem você quer transferir R$ 10,00{" "}
                    </Text>
                    <Text>
                      <Text style={{ fontWeight: "900" }}>
                        Encontre um contato
                      </Text>{" "}
                      na sua lista ou inicie uma{" "}
                      <Text style={{ fontWeight: "900" }}>
                        {" "}
                        nova transferência
                      </Text>
                    </Text>
                    <View style={stylesValue.container}>
                      <TextInput
                        style={stylesValue.input}
                        keyboardType="default"
                        maxLength={15}
                        placeholder="Nome,CPF/CNPJ ou chave Pix"
                      />
                    </View>

                    <LinhaDivisoria />
                    <Text style={{ fontWeight: "700", fontSize: 16 }}>
                      Contato Frequentes
                    </Text>
                    <View style={{ alignItems: "center" }}>
                      <ScrollView
                        horizontal
                        showsHorizontalScrollIndicator={false}
                        contentContainerStyle={stylesSection.containerScrol}
                      >
                        <View style={stylesSection.contentOptions}>
                          <TouchableOpacity
                            onPress={() => router.navigate("/confirmar_pix")}
                            style={stylesSection.circuloOptions}
                          >
                            <Text style={{ fontSize: 30, fontWeight: 600 }}>
                              AR
                            </Text>
                          </TouchableOpacity>
                          <Text style={stylesSection.titleOptions}>
                            Arthur Rangel
                          </Text>
                          <Text>CAIXA...</Text>
                        </View>

                        <View style={stylesSection.contentOptions}>
                          <TouchableOpacity
                            onPress={() => router.navigate("/")}
                            style={stylesSection.circuloOptions}
                          >
                            <Text style={{ fontSize: 30, fontWeight: 600 }}>
                              LL
                            </Text>
                          </TouchableOpacity>
                          <Text style={stylesSection.titleOptions}>
                            Luiz Lopes
                          </Text>
                          <Text>CAIXA...</Text>
                        </View>

                        <View style={stylesSection.contentOptions}>
                          <TouchableOpacity
                            onPress={() => router.navigate("/")}
                            style={stylesSection.circuloOptions}
                          >
                            <Text style={{ fontSize: 30, fontWeight: 600 }}>
                              FC
                            </Text>
                          </TouchableOpacity>
                          <Text style={stylesSection.titleOptions}>
                            Felipe Carvalho
                          </Text>
                          <Text>NU PAGAMENTOS...</Text>
                        </View>
                      </ScrollView>
                    </View>
                    <Text style={{ fontWeight: "700", fontSize: 16 }}>
                      Todos os contatos
                    </Text>
                    <View style={{ alignItems: "left" }}>
                      <ScrollView
                        Vertical
                        showsHorizontalScrollIndicator={false}
                        contentContainerStyle={styleslist.containerScrol}
                      >
                        <View style={styleslist.contentOptions}>
                          <View style={styleslist.contentOptions}>
                            <TouchableOpacity
                              onPress={() => router.navigate("/confirmar_pix")}
                              style={styleslist.circuloOptions}
                            >
                              <Text style={{ fontSize: 16, fontWeight: 900 }}>
                                AR
                              </Text>
                            </TouchableOpacity>
                            <Text style={styleslist.titleOptions}>
                              Arthur Rangel
                            </Text>
                          </View>
                        </View>

                        <View style={styleslist.contentOptions}>
                          <View style={styleslist.contentOptions}>
                            <TouchableOpacity
                              onPress={() => router.navigate("/")}
                              style={styleslist.circuloOptions}
                            >
                              <Text style={{ fontSize: 16, fontWeight: 900 }}>
                                GS
                              </Text>
                            </TouchableOpacity>
                            <Text style={styleslist.titleOptions}>
                              Gabriel Henrique da Silva
                            </Text>
                          </View>
                        </View>
                        <View style={styleslist.contentOptions}>
                          <View style={styleslist.contentOptions}>
                            <TouchableOpacity
                              onPress={() => router.navigate("/")}
                              style={styleslist.circuloOptions}
                            >
                              <Text style={{ fontSize: 16, fontWeight: 900 }}>
                                RS
                              </Text>
                            </TouchableOpacity>
                            <Text style={styleslist.titleOptions}>
                              Ricardo Antônio Fernandes Souza
                            </Text>
                          </View>
                        </View>

                        <View style={styleslist.contentOptions}>
                          <View style={styleslist.contentOptions}>
                            <TouchableOpacity
                              onPress={() => router.navigate("/")}
                              style={styleslist.circuloOptions}
                            >
                              <Text style={{ fontSize: 16, fontWeight: 900 }}>
                                BA
                              </Text>
                            </TouchableOpacity>
                            <Text style={styleslist.titleOptions}>
                              Beatriz Mendes de Almeida
                            </Text>
                          </View>
                        </View>
                      </ScrollView>
                    </View>
                  </View>
                </View>
              </View>
            </View>
          </ScrollView>
        </SafeAreaView>
      </SafeAreaProvider>
    </>
  )
}

const styles = StyleSheet.create({
  container: {
    height: "auto",
    alignItems: "center",
    backgroundColor: "#fff",
  },

  cabecalho: {
    flex: 1,
    backgroundColor: "#ffffff",
    width: "100%",
    height: 178,
    paddingHorizontal: 20,
  },

  icone: {
    width: 20,
    height: 20,
  },

  boxIconesCabecalho: {
    flexDirection: "column",
    justifyContent: "space-between",
    marginTop: 53,
  },

  itensIcones: {
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
    gap: 15,
  },

  boxTextUsuario: {
    marginTop: 20,
  },

  textTitle: {
    color: "Black",
    fontSize: 30,
    fontWeight: "bold",
    marginTop: 15,
  },
  linha: {
    borderBottomWidth: 1,
    borderBottomColor: "gray",
    width: "100%",
    alignSelf: "center",
    paddingVertical: 10,
  },
})




const styleslist = StyleSheet.create({
  containerScrol: {
    marginTop: 10,
    alignItems: "left",
    gap: 20,
  },

  contentOptions: {
    alignItems: "left",
    justifyContent: "left",
    marginHorizontal: 0,
    flexDirection: "row",
  },
  circuloOptions: {
    width: 60,
    height: 60,
    marginLeft: 0,
    backgroundColor: "#f0f1f5",
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 150,
  },
  titleOptions: {
    fontSize: 16,
    fontWeight: 500,
    marginLeft: 10,
    paddingTop: 17,
  },
})

  const stylesSection = StyleSheet.create({
    container: {
      flex: 1,
      height: "100%",
      alignItems: "center",
      justifyContent: "space-between",
      // marginBottom: 20,
    },

    content: {
      backgroundColor: "#fff",
      width: "100%",
      paddingHorizontal: 20,
    },

    title: {
      marginTop: 20,
      fontSize: 22,
      fontWeight: 500,
    },

    titleOptions: {
      fontSize: 14,
      fontWeight: 500,
    },

    titleSaldo: {
      fontSize: 26,
      fontWeight: 700,
    },

    containerScrol: {
      marginTop: 40,
      alignItems: "center",
    },

    contentOptions: {
      alignItems: "center",
      justifyContent: "center",
      marginHorizontal: 10,
    },

    circuloOptions: {
      width: 90,
      height: 90,
      marginLeft: 0,
      backgroundColor: "#f0f1f5",
      justifyContent: "center",
      alignItems: "center",
      borderRadius: 150,
    
    },

    cartoes: {
      backgroundColor: "#ffffff",
      flexDirection: "row",
      gap: 10,

      width: "100%",
      height: 56,
      borderRadius: 12,

      padding: 16,
    },

    inforRend: {
      backgroundColor: "#f0f1f5",

      width: 263,
      height: 80,
      borderRadius: 12,

      paddingTop: 16,
      paddingLeft: 16,
      paddingRight: 16,
      paddingBottom: 10,
    },
  })
const stylesValue = StyleSheet.create({
  container: {
    flexDirection: "row",
    alignItems: "center",
    width: "100%",
    marginTop: 5,
    
  },
  currency: {
    fontSize: 22,
    fontWeight: "700",
    marginRight: 5,
  },
  input: {
    fontSize: 22,
    fontWeight: "700",
    borderWidth: 0,
    flex: 1,
    marginBottom:-40
  },
})