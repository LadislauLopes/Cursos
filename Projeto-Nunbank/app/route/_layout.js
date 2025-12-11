import { Stack } from 'expo-router';
import React from 'react';


export default function RootLayout() {
    return (
      <Stack>
        <Stack.Screen name="index" options={{ headerShown: false }} />
        <Stack.Screen name="sobre" options={{ headerShown: false }} />
        <Stack.Screen name="tela_valor_pix" options={{ headerShown: false }} />
        <Stack.Screen name="tela_aprovado" options={{ headerShown: false }} />
        <Stack.Screen name="tela_digita_pix" options={{ headerShown: false }} />
        <Stack.Screen name="confirmar_pix" options={{ headerShown: false }} />
      </Stack>
    )
}