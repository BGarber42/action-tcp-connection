# action-tcp-connection

GitHub Action to make a TCP connection with retry logic and comprehensive error handling.

[![Github Action - TCP Test](https://github.com/BGarber42/action-tcp-connection/actions/workflows/main.yml/badge.svg)](https://github.com/BGarber42/action-tcp-connection/actions/workflows/main.yml)

## Features

- TCP connection testing with automatic retry logic
- Comprehensive input validation
- Detailed error reporting
- Configurable timeout settings
- Support for custom content transmission

## Usage

### Basic Usage

```yaml
- name: Test TCP Connection
  uses: BGarber42/action-tcp-connection@main
  with:
    remotehost: 'example.com'
    remoteport: '80'
```

### Advanced Usage

```yaml
- name: Test TCP Connection with Custom Timeout
  uses: BGarber42/action-tcp-connection@main
  with:
    remotehost: '192.168.1.100'
    remoteport: '8080'
    maxtime: '120'
```

## Inputs

| Parameter | Description | Required | Default |
|-----------|-------------|----------|---------|
| `remotehost` | IP address or hostname to connect to | Yes | `127.0.0.1` |
| `remoteport` | Port number to connect to (1-65535) | Yes | `80` |
| `maxtime` | Maximum time in seconds to retry connection | No | `60` |

## Outputs

| Parameter | Description |
|-----------|-------------|
| `myOutput` | Success message when connection is established |
| `error` | Error message if connection fails |

## Error Handling

The action includes comprehensive error handling for:
- Invalid hostnames or IP addresses
- Invalid port numbers
- Connection timeouts
- Network errors
- Input validation errors

## Best Practices

1. Always specify the exact host and port you want to test
2. Use appropriate timeout values for your network conditions
3. Handle the error output in your workflow for better debugging
4. Consider using this action in CI/CD pipelines to verify service availability
