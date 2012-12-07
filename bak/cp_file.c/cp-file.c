#include <stdio.h>
#include <stdlib.h>

#define DEBUG		188
#define BUFFER_SIZE	256
#define WR_ERR		-2
#define WR_OK		0;

int cp_file( const char* in, const char* out, int size ){
    FILE* fin = fopen( in, "br");
    FILE* fout = fopen( out, "br" );
    //char* buffer = malloc( size*2 );
    char buffer[ BUFFER_SIZE ];
    int len = 0;
    int size_r = 0, size_w = 0;
    
    if( size == DEBUG ){
	printf( "DEBUG\n" );
	return -1;
    }

    while( ( size_r = fread( buffer, 1, size , fin  ) ) > 0 ){
	printf( "File open ok\n" );
	size_w = fread( buffer, 1, size , fout );
	if( size_r != size_w ){
	    perror( "Fatal write error\n" );
	    return WR_ERR;
	}
	len += size_w;
	printf( "coping file... %d bytes copied\n", len );
    }
    
    fclose( fin );
    fclose( fout );
    return WR_OK;
}

int main( int argc, char* agrv ){
    cp_file( "fin.txt", "fout.txt", BUFFER_SIZE );
    //cp_file( "fin.txt", "fout.txt", DEBUG );
    return 0;
}
