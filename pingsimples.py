import os #Importa o modulo ou biblioteca "os"(integra os programas e recursos do s.o

print('#' * 60) #imprimindo 60 vezes

ip_ou_host = input('Digite o Ip ou host a ser verificado: ') #criamos uma variavel que vai receber do usuario um ip
print('-' * 60)
os.system('ping -n 6 {}'.format(ip_ou_host)) #chamando system da biblioteca os - comando ping
# -n -num de pacotes que serão 6 {}
print('-' * 60)