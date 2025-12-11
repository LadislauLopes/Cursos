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

import React, { useState } from "react"

const LinhaDivisoria = () => {
  return <View style={styles.linha} />
}

export default function Sobre() {
  const router = useRouter()
  const [inputValue, setInput] = useState("")
  const [balance, setBalance] = useState("R$40.221,00")
  const [limitCard, setLimit] = useState("R$80.500,00")

  const formatCurrency = (value) => {
    const numericValue = value.replace(/\D/g, "")
    const number = parseInt(numericValue || "0", 10)
    const formatted = (number / 100).toLocaleString("pt-BR", {
      style: "currency",
      currency: "BRL",
    })
    return formatted.replace("R$", "").trim()
  }

  const handleInputChange = (value) => {
    setInput(formatCurrency(value))
  }

  return (
    <SafeAreaProvider>
      <SafeAreaView style={{ flex: 1, backgroundColor: "#fff" }}>
        <StatusBar barStyle="dark-content" translucent />

        {/* Conteúdo principal com Scroll */}
        <ScrollView contentContainerStyle={{ paddingBottom: 100 }}>
          {/* Header */}
          <View style={styles.cabecalho}>
            <View style={styles.boxIconesCabecalho}>
              <TouchableOpacity onPress={() => router.back()}>
                <Image
                  style={styles.icone}
                  source={require("./img/botao-x.png")}
                />
              </TouchableOpacity>

              <Text style={styles.textTitle}>
                Qual é o valor da Transferência?
              </Text>
              <Text style={{ marginVertical: 5 }}>
                Saldo da conta:{" "}
                <Text style={{ fontWeight: 800 }}> {balance}</Text>
              </Text>
              <Text style={{ marginVertical: 5 }}>
                Limite do cartão: <Text style={{ fontWeight: 800 }}>{limitCard}</Text>
              </Text>
            </View>

            <View style={stylesValue.container}>
              <Text style={stylesValue.currency}>R$</Text>
              <TextInput
                style={stylesValue.input}
                keyboardType="numeric"
                onChangeText={handleInputChange}
                value={inputValue}
                maxLength={15}
                placeholder="0,00"
              />
            </View>

            <LinhaDivisoria />
          </View>
        </ScrollView>

        {/* Botão Fixo no Rodapé */}
        <View style={stylesSection.container}>
          <TouchableOpacity
            style={stylesSection.circuloOptions}
            onPress={() => router.navigate("tela_digita_pix")}
          >
            <Image
              style={styles.icone}
              source={require("./img/pix/next.png")}
            />
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
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
    marginTop: 10,
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
  },
})

const stylesSection = StyleSheet.create({
  container: {
    position: "absolute",
    bottom: 20, // Mantém na parte inferior
    right: 20, // Mantém na direita
  },

  circuloOptions: {
    backgroundColor: "#8A19D6",
    width: 53,
    height: 53,
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 100,
  },

  icone: {
    width: 20,
    height: 20,
  },
})
