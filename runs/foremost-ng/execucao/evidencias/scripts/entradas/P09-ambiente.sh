# Registro complementar do ambiente (protocolo §6.3): SO, kernel, CPU, RAM, disco, versões.
uname -a
nproc
lscpu | grep -E "Model name|^CPU\(s\)|Thread|Core|Socket|Hypervisor"
free -b
df -h / /home
ldd --version | head -1
ld --version | head -1
gcc --version | head -1
make --version | head -1
openssl version
curl-config --version
git --version
dpkg -l libc6-dev gcc-13 libssl3t64 libcurl4t64 | tail -4
