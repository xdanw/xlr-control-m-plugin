
# Control-M Integration for XL Release

![GitHub release](https://img.shields.io/github/release/xebialabs-community/xlr-control-m-plugin.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Github All Releases](https://img.shields.io/github/downloads/xebialabs-community/xlr-control-m-plugin/total.svg)](https://github.com/xebialabs-community/xlr-control-m-plugin/releases)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-blue.svg)](https://github.com/RichardLitt/standard-readme)

## Installation

### Requirements

1. XL Release 9.0+

### Building the plugin
The gradle wrapper facilitates building the plugin.  Use the following command to build using [Gradle](https://gradle.org/):
```bash
./gradlew clean build
```
The built plugin, along with other files from the build, can then be found in the _build_ folder.

### Adding the plugin to XL Release

Download the latest version of the plugin from the [releases page](https://github.com/xebialabs-community/xlr-control-m-plugin/releases).  The plugin can then be installed through the XL Release graphical interface or the server backend.  For additional detail, please refer to [the docs.xebialabs.com documentation on XLR plugin installation](https://docs.xebialabs.com/xl-release/how-to/install-or-remove-xl-release-plugins.html)

## Usage

__Available Tasks__: Check Latest Job

__Available Triggers__: None

__Available Dashboard Tiles__: None

### Tasks

#### Check Latest Job
Properties:
* Server _input_ 
* Username _input_ 
   * Optionally, override the username used to connect to the server
* Password _input_ 
   * Optionally, override the password used to connect to the server
* Job Name _input_ 
   * Optionally, provide a job name filter
* Folder _input_ 
   * Optionally, provide a folder filter
* Ctm _input_ 
   * Optionally, provide a ctm filter
* Application _input_ 
   * Optionally, provide an application filter
* SubApplication _input_ 
   * Optionally, provide a subapplication filter
* Host _input_ 
   * Optionally, provide a host filter
* Description _input_ 
   * Optionally, provide a description filter
* Job ID _input_ 
   * Optionally, provide a job id filter
* Poll Frequency _input_ 
   * Specify the frequency at which to poll for Control-M job information
* Job ID _output_ 
* Status _output_ 
* Output URI _output_ 
* Log URI _output_ 

## Contributing

Please review the contributing guidelines for _xebialabs-community_ at [http://xebialabs-community.github.io/](http://xebialabs-community.github.io/)

## License

This community plugin is licensed under the [MIT license](https://opensource.org/licenses/MIT).

See license in [LICENSE.md](LICENSE.md)
