
Vagrant.configure("2") do |config|
  config.vm.box = "generic/rocky9"
  config.vm.network "private_network", ip: "10.3.1.56"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 1024
    vb.cpus = 2
  end
end
