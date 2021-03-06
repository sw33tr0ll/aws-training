# The AWS CLI
Command-line access to Amazon Web Services. Let's get started!

## Installing on Windows
Download and run the MSI installer from https://awscli.amazonaws.com/AWSCLIV2.msi

## Installing on Linux
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 
unzip awscliv2.zip 
sudo ./aws/install 
```

## Testing your Installation
```
aws --version
```

# Creating API Keys
>[https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration)

To use the CLI, you need API keys. Get some by logging in to the [IAM console](https://console.aws.amazon.com/iam).

{% include googleDrivePlayer.html id=1kJ2D99Scgtz2jbvJPQg1MbDeu2DYDzDm %}

> 1. Click "users"
> 2. Add a user
> 3. Give the user programmatic access
> 4. Add the user to the _Admins_ group
> 5. Save the keys somewhere _safe_

# Configuring the CLI
Run the **aws configure** command. Enter your API keys and region. 

> IMAGE

AWS saves the keys locally at ~/.aws/credentials.

> IMAGE

You can test your configuration by running a command. For example:

> IMAGE

Now that the CLI is up and running, let's take it for a spin! AWS CLI commands are usually formatted like:

```
aws <command> <subcommands>
```

## aws help
Consult the help info often. The **aws help** command by itself will list the command line options and the different commands

```aws help```

Each command will have it's own help menu with a list of subcommands and other options. You can see these by typing:

```aws <command> help```
