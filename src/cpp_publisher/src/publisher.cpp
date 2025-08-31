#include "rclcpp/rclcpp.hpp"

class PublisherNode : public rclcpp::Node 
{
public:
    PublisherNode() : Node("publisher") {
        RCLCPP_INFO(this->get_logger(), "HELLO!");
    }
};


int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}