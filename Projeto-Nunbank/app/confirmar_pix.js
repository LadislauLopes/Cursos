import React, { useState } from "react"
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Switch,
  Image,
} from "react-native"
import { MaterialIcons } from "@expo/vector-icons"
import { useRouter } from "expo-router"


export default function TransferScreen() {
  const [trusted, setTrusted] = useState(false)
  const router = useRouter()
  return (
    <View style={styles.container}>
      <TouchableOpacity onPress={() => router.back()}>
        <Image style={styles.icone} source={require("./img/botao-x.png")} />
      </TouchableOpacity>

      <Text style={styles.title}>Transferindo</Text>
      <Text style={styles.amount}>R$ 10,00</Text>
      <Text style={styles.recipient}>
        para <Text style={styles.bold}>Arthur Rangel</Text>
      </Text>

      <TouchableOpacity style={styles.messageButton}>
        <MaterialIcons name="message" size={16} color="#7F7F7F" />
        <Text style={styles.messageText}>Escrever uma mensagem...</Text>
      </TouchableOpacity>

      <View style={styles.infoBox}>
        <Text style={styles.infoText}>CPF: ***.219.752-**</Text>
        <Text style={styles.infoText}>Instituição: NU PAGAMENTOS - IP</Text>
      </View>

      <View style={styles.trustedBox}>
        <Switch value={trusted} onValueChange={setTrusted} />
        <Text style={styles.trustedText}>
          Adicionar contato à minha lista de confiança para fazer Pix sem
          complicações no futuro.
        </Text>
      </View>

      <TouchableOpacity
        style={styles.transferButton}
        onPress={() => router.navigate("/tela_aprovado")}
      >
        <Text style={styles.transferButtonText}>Transferir</Text>
      </TouchableOpacity>
    </View>
  )
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#fff", padding: 20 },
  title: { color: "#000", fontSize: 18, marginBottom: 10 },
  amount: { color: "#8A19D6", fontSize: 32, fontWeight: "bold" },
  recipient: { color: "#000", fontSize: 16, marginTop: 5 },
  bold: { fontWeight: "bold" },
  messageButton: {
    flexDirection: "row",
    alignItems: "center",
    marginVertical: 10,
  },
  messageText: { color: "#7F7F7F", marginLeft: 5 },
  infoBox: {
    backgroundColor: "#fff",
    padding: 10,
    borderRadius: 8,
    marginVertical: 10,
  },
  infoText: { color: "black" },
  trustedBox: {
    flexDirection: "row",
    alignItems: "center",
    marginVertical: 10,
  },
  trustedText: { color: "#CCC", marginLeft: 10, flex: 1 },
  transferButton: {
    backgroundColor: "#7D34E3",
    padding: 15,
    borderRadius: 8,
    alignItems: "center",
    marginTop: 20,
  },
  transferButtonText: { color: "#FFF", fontSize: 16, fontWeight: "bold" },
  icone: {
    width: 20,
    height: 20,
  },
})
