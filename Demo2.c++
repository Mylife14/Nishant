#include <iostream>
#include <boost/asio.hpp>

using namespace boost::asio;
using ip::tcp;

int main() {
    io_service io;
    
    // Create an endpoint to accept connections on port 8080
    tcp::acceptor acceptor(io, tcp::endpoint(tcp::v4(), 8080));
    
    std::cout << "Server started on port 8080" << std::endl;
    
    while(true) {
        // Create a socket
        tcp::socket socket(io);
        
        // Wait and accept a connection
        acceptor.accept(socket);
        
        // Write a simple HTTP response to the client
        std::string message = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\nHello, World!";
        boost::system::error_code ignored_error;
        write(socket, buffer(message), ignored_error);
    }

    return 0;
}
