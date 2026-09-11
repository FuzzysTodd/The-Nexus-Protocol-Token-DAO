
    def test_withdraw_js_runtime_labels_transaction_direction():
>       output = run_node(
            """
            const withdraw = require('./withdraw.js');
            const wallet = '0xeCE999c86452c573Adfdd7F0C9226e673477973a';
            const parsed = withdraw.parseImportedPayload(JSON.stringify({
              wallet_address: wallet,
              transactions: [
                {
                  chain: 'ethereum',
                  transaction_type: 'Sent USDT',
                  from: wallet,
                  to: '0x1111111111111111111111111111111111111111',
                  amount: '1000000',
                  decimals: 6,
                  symbol: 'USDT'
                },
                {
                  chain: 'ethereum',
                  transaction_type: 'Received USDT',
                  from: '0x1111111111111111111111111111111111111111',
                  to: wallet,
                  amount: '2000000',
                  decimals: 6,
                  symbol: 'USDT'
                }
              ]
            }));
            console.log(JSON.stringify(parsed.transactions.map(tx => ({
              direction: tx.direction,
              directionLabel: tx.directionLabel,
              recipientStatus: tx.recipientStatus,
              recipientLabel: tx.recipientLabel,
              recipientWarning: tx.recipientWarning,
              amountLabel: tx.amountLabel
            }))));
            """
        )

nexus/test_withdraw_dashboard.py:221: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
nexus/test_withdraw_dashboard.py:14: in run_node
    result = subprocess.run(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = True, timeout = None, check = True
popenargs = (['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const wallet = '0xeCE999...\n          recipientWarning: tx.recipientWarning,\n          amountLabel: tx.amountLabel\n        }))));\n        "],)
kwargs = {'cwd': PosixPath('/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA'), 'stderr': -1, 'stdout': -1, 'text': True}
process = <Popen: returncode: 1 args: ['/usr/local/bin/node', '-e', "\n        const w...>
stdout = ''
stderr = '/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA/withdraw.js:101\npragma solidity ^0.8.20;...les/helpers:147:16)\n    at [eval]:2:26\n    at runScriptInThisContext (node:internal/vm:209:10)\n\nNode.js v22.22.3\n'
retcode = 1

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.
    
        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.
    
        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.
    
        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.
    
        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.
    
        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.
    
        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE
    
        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE
    
        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const wallet = '0xeCE999c86452c573Adfdd7F0C9226e673477973a';\n        const parsed = withdraw.parseImportedPayload(JSON.stringify({\n          wallet_address: wallet,\n          transactions: [\n            {\n              chain: 'ethereum',\n              transaction_type: 'Sent USDT',\n              from: wallet,\n              to: '0x1111111111111111111111111111111111111111',\n              amount: '1000000',\n              decimals: 6,\n              symbol: 'USDT'\n            },\n            {\n              chain: 'ethereum',\n              transaction_type: 'Received USDT',\n              from: '0x1111111111111111111111111111111111111111',\n              to: wallet,\n              amount: '2000000',\n              decimals: 6,\n              symbol: 'USDT'\n            }\n          ]\n        }));\n        console.log(JSON.stringify(parsed.transactions.map(tx => ({\n          direction: tx.direction,\n          directionLabel: tx.directionLabel,\n          recipientStatus: tx.recipientStatus,\n          recipientLabel: tx.recipientLabel,\n          recipientWarning: tx.recipientWarning,\n          amountLabel: tx.amountLabel\n        }))));\n        "]' returned non-zero exit status 1.

/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/subprocess.py:571: CalledProcessError
________ test_withdraw_js_runtime_helpers_cover_formatting_and_parsing _________

    def test_withdraw_js_runtime_helpers_cover_formatting_and_parsing():
>       output = run_node(
            """
            const withdraw = require('./withdraw.js');
            const validPayload = withdraw.parseImportedPayload(JSON.stringify({
              wallet_address: '0xabc',
              balances: [{
                chain: 'ethereum',
                address: 'native',
                amount: '1500000000000000000',
                symbol: 'ETH',
                decimals: 18,
                value_usd: 3200
              }]
            }));
            const invalidJson = (() => {
              try { withdraw.parseImportedPayload('{'); } catch (error) { return error.message; }
            })();
            const nonObject = (() => {
              try { withdraw.parseImportedPayload('[]'); } catch (error) { return error.message; }
            })();
            const emptyPayload = (() => {
              try {
                withdraw.parseImportedPayload(JSON.stringify({ balances: [], transactions: [] }));
              } catch (error) {
                return error.message;
              }
            })();
            console.log(JSON.stringify({
              large: withdraw.formatTokenAmount('1000000000000', 6),
              medium: withdraw.formatTokenAmount('1500000', 6),
              small: withdraw.formatTokenAmount('12345', 8),
              wallet: validPayload.walletAddress,
              balances: validPayload.balances.length,
              invalidJson,
              nonObject,
              emptyPayload
            }));
            """
        )

nexus/test_withdraw_dashboard.py:280: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
nexus/test_withdraw_dashboard.py:14: in run_node
    result = subprocess.run(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = True, timeout = None, check = True
popenargs = (['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const validPayload = wit...load.balances.length,\n          invalidJson,\n          nonObject,\n          emptyPayload\n        }));\n        "],)
kwargs = {'cwd': PosixPath('/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA'), 'stderr': -1, 'stdout': -1, 'text': True}
process = <Popen: returncode: 1 args: ['/usr/local/bin/node', '-e', "\n        const w...>
stdout = ''
stderr = '/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA/withdraw.js:101\npragma solidity ^0.8.20;...les/helpers:147:16)\n    at [eval]:2:26\n    at runScriptInThisContext (node:internal/vm:209:10)\n\nNode.js v22.22.3\n'
retcode = 1

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.
    
        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.
    
        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.
    
        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.
    
        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.
    
        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.
    
        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE
    
        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE
    
        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const validPayload = withdraw.parseImportedPayload(JSON.stringify({\n          wallet_address: '0xabc',\n          balances: [{\n            chain: 'ethereum',\n            address: 'native',\n            amount: '1500000000000000000',\n            symbol: 'ETH',\n            decimals: 18,\n            value_usd: 3200\n          }]\n        }));\n        const invalidJson = (() => {\n          try { withdraw.parseImportedPayload('{'); } catch (error) { return error.message; }\n        })();\n        const nonObject = (() => {\n          try { withdraw.parseImportedPayload('[]'); } catch (error) { return error.message; }\n        })();\n        const emptyPayload = (() => {\n          try {\n            withdraw.parseImportedPayload(JSON.stringify({ balances: [], transactions: [] }));\n          } catch (error) {\n            return error.message;\n          }\n        })();\n        console.log(JSON.stringify({\n          large: withdraw.formatTokenAmount('1000000000000', 6),\n          medium: withdraw.formatTokenAmount('1500000', 6),\n          small: withdraw.formatTokenAmount('12345', 8),\n          wallet: validPayload.walletAddress,\n          balances: validPayload.balances.length,\n          invalidJson,\n          nonObject,\n          emptyPayload\n        }));\n        "]' returned non-zero exit status 1.

/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/subprocess.py:571: CalledProcessError
______ test_withdraw_js_runtime_builds_imported_balance_transfer_requests ______

    def test_withdraw_js_runtime_builds_imported_balance_transfer_requests():
>       output = run_node(
            """
            const withdraw = require('./withdraw.js');
            const readyBalance = {
              assetType: 'balance',
              chain: 'base',
              chainId: 8453,
              address: '0x1234',
              rawAmount: '2500000',
              offRamp: {
                status: 'ready',
                settlement: {
                  network: 'Base',
                  supportsDirectTransfer: true
                }
              }
            };
            const nativeBalance = {
              assetType: 'balance',
              chain: 'ethereum',
              chainId: 1,
              address: 'native',
              rawAmount: '1000000000000000000',
              offRamp: {
                status: 'ready',
                settlement: {
                  network: 'Ethereum',
                  supportsDirectTransfer: true
                }
              }
            };
            const reviewBalance = {
              assetType: 'balance',
              chain: 'base',
              chainId: 8453,
              address: '0x9999',
              rawAmount: '1',
              offRamp: {
                status: 'review',
                settlement: {
                  network: 'Base',
                  supportsDirectTransfer: true
                }
              }
            };
            const tokenRequest = withdraw.buildImportedBalanceTransferRequest(
              readyBalance,
              '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac'
            );
            const nativeRequest = withdraw.buildImportedBalanceTransferRequest(
              nativeBalance,
              '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac'
            );
            const invalidStatus = withdraw.validateImportedBalanceTransfer(
              reviewBalance,
              '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac',
              8453
            );
            const wrongChain = withdraw.validateImportedBalanceTransfer(
              readyBalance,
              '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac',
              1
            );
            console.log(JSON.stringify({
              canSendReady: withdraw.canSendImportedBalance(readyBalance),
              canSendReview: withdraw.canSendImportedBalance(reviewBalance),
              tokenRequest,
              nativeRequest,
              invalidStatus,
              wrongChain
            }));
            """
        )

nexus/test_withdraw_dashboard.py:335: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
nexus/test_withdraw_dashboard.py:14: in run_node
    result = subprocess.run(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = True, timeout = None, check = True
popenargs = (['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const readyBalance = {\n...    tokenRequest,\n          nativeRequest,\n          invalidStatus,\n          wrongChain\n        }));\n        "],)
kwargs = {'cwd': PosixPath('/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA'), 'stderr': -1, 'stdout': -1, 'text': True}
process = <Popen: returncode: 1 args: ['/usr/local/bin/node', '-e', "\n        const w...>
stdout = ''
stderr = '/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA/withdraw.js:101\npragma solidity ^0.8.20;...les/helpers:147:16)\n    at [eval]:2:26\n    at runScriptInThisContext (node:internal/vm:209:10)\n\nNode.js v22.22.3\n'
retcode = 1

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.
    
        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.
    
        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.
    
        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.
    
        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.
    
        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.
    
        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE
    
        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE
    
        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const readyBalance = {\n          assetType: 'balance',\n          chain: 'base',\n          chainId: 8453,\n          address: '0x1234',\n          rawAmount: '2500000',\n          offRamp: {\n            status: 'ready',\n            settlement: {\n              network: 'Base',\n              supportsDirectTransfer: true\n            }\n          }\n        };\n        const nativeBalance = {\n          assetType: 'balance',\n          chain: 'ethereum',\n          chainId: 1,\n          address: 'native',\n          rawAmount: '1000000000000000000',\n          offRamp: {\n            status: 'ready',\n            settlement: {\n              network: 'Ethereum',\n              supportsDirectTransfer: true\n            }\n          }\n        };\n        const reviewBalance = {\n          assetType: 'balance',\n          chain: 'base',\n          chainId: 8453,\n          address: '0x9999',\n          rawAmount: '1',\n          offRamp: {\n            status: 'review',\n            settlement: {\n              network: 'Base',\n              supportsDirectTransfer: true\n            }\n          }\n        };\n        const tokenRequest = withdraw.buildImportedBalanceTransferRequest(\n          readyBalance,\n          '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac'\n        );\n        const nativeRequest = withdraw.buildImportedBalanceTransferRequest(\n          nativeBalance,\n          '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac'\n        );\n        const invalidStatus = withdraw.validateImportedBalanceTransfer(\n          reviewBalance,\n          '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac',\n          8453\n        );\n        const wrongChain = withdraw.validateImportedBalanceTransfer(\n          readyBalance,\n          '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac',\n          1\n        );\n        console.log(JSON.stringify({\n          canSendReady: withdraw.canSendImportedBalance(readyBalance),\n          canSendReview: withdraw.canSendImportedBalance(reviewBalance),\n          tokenRequest,\n          nativeRequest,\n          invalidStatus,\n          wrongChain\n        }));\n        "]' returned non-zero exit status 1.

/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/subprocess.py:571: CalledProcessError
_______ test_withdraw_js_runtime_can_normalize_dune_collectibles_payload _______

    def test_withdraw_js_runtime_can_normalize_dune_collectibles_payload():
>       output = run_node(
            """
            const withdraw = require('./withdraw.js');
            const imported = withdraw.parseImportedPayload(JSON.stringify({
              address: '0xd8da6bf26964af9d7eed9e03e53415d37aa96045',
              entries: [{
                contract_address: '0x1234',
                token_standard: 'ERC721',
                token_id: '1',
                chain: 'base',
                chain_id: 8453,
                name: 'Base Genesis',
                symbol: 'BG',
                balance: '1',
                is_spam: false,
                last_acquired: '2026-04-06T18:15:47+00:00'
              }, {
                contract_address: '0xabcd',
                token_standard: 'ERC1155',
                token_id: '9',
                chain: 'ethereum',
                chain_id: 1,
                name: 'Spam Drop',
                symbol: 'DROP',
                balance: '2',
                is_spam: true
              }]
            }));
            console.log(JSON.stringify({
              wallet: imported.walletAddress,
              source: imported.source,
              balances: imported.balances.length,
              collectibles: imported.collectibles.length,
              baseNetwork: imported.collectibles[0].offRamp.settlement.network,
              baseDestination: imported.collectibles[0].offRamp.settlement.destination,
              spamStatus: imported.collectibles[1].offRamp.status
            }));
            """
        )

nexus/test_withdraw_dashboard.py:421: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
nexus/test_withdraw_dashboard.py:14: in run_node
    result = subprocess.run(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = True, timeout = None, check = True
popenargs = (['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const imported = withdra...Ramp.settlement.destination,\n          spamStatus: imported.collectibles[1].offRamp.status\n        }));\n        "],)
kwargs = {'cwd': PosixPath('/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA'), 'stderr': -1, 'stdout': -1, 'text': True}
process = <Popen: returncode: 1 args: ['/usr/local/bin/node', '-e', "\n        const w...>
stdout = ''
stderr = '/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA/withdraw.js:101\npragma solidity ^0.8.20;...les/helpers:147:16)\n    at [eval]:2:26\n    at runScriptInThisContext (node:internal/vm:209:10)\n\nNode.js v22.22.3\n'
retcode = 1

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.
    
        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.
    
        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.
    
        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.
    
        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.
    
        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.
    
        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE
    
        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE
    
        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const imported = withdraw.parseImportedPayload(JSON.stringify({\n          address: '0xd8da6bf26964af9d7eed9e03e53415d37aa96045',\n          entries: [{\n            contract_address: '0x1234',\n            token_standard: 'ERC721',\n            token_id: '1',\n            chain: 'base',\n            chain_id: 8453,\n            name: 'Base Genesis',\n            symbol: 'BG',\n            balance: '1',\n            is_spam: false,\n            last_acquired: '2026-04-06T18:15:47+00:00'\n          }, {\n            contract_address: '0xabcd',\n            token_standard: 'ERC1155',\n            token_id: '9',\n            chain: 'ethereum',\n            chain_id: 1,\n            name: 'Spam Drop',\n            symbol: 'DROP',\n            balance: '2',\n            is_spam: true\n          }]\n        }));\n        console.log(JSON.stringify({\n          wallet: imported.walletAddress,\n          source: imported.source,\n          balances: imported.balances.length,\n          collectibles: imported.collectibles.length,\n          baseNetwork: imported.collectibles[0].offRamp.settlement.network,\n          baseDestination: imported.collectibles[0].offRamp.settlement.destination,\n          spamStatus: imported.collectibles[1].offRamp.status\n        }));\n        "]' returned non-zero exit status 1.

/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/subprocess.py:571: CalledProcessError
__________ test_withdraw_js_runtime_settlement_destination_validation __________

    def test_withdraw_js_runtime_settlement_destination_validation():
>       output = run_node(
            """
            global.document = {
              getElementById: () => ({ value: '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac' })
            };
            global.ethers = {
              utils: {
                isAddress: (value) => /^0x[a-fA-F0-9]{40}$/.test(value)
              }
            };
            const withdraw = require('./withdraw.js');
            const valid = withdraw.getSettlementDestination();
            global.document = {
              getElementById: () => ({ value: '   ' })
            };
            const blank = withdraw.getSettlementDestination();
            global.document = {
              getElementById: () => ({ value: 'not-an-address' })
            };
            const invalid = withdraw.getSettlementDestination();
            console.log(JSON.stringify({ valid, blank, invalid }));
            """
        )

nexus/test_withdraw_dashboard.py:471: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
nexus/test_withdraw_dashboard.py:14: in run_node
    result = subprocess.run(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = True, timeout = None, check = True
popenargs = (['/usr/local/bin/node', '-e', "\n        global.document = {\n          getElementById: () => ({ value: '0x1EF9950fc2...d = withdraw.getSettlementDestination();\n        console.log(JSON.stringify({ valid, blank, invalid }));\n        "],)
kwargs = {'cwd': PosixPath('/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA'), 'stderr': -1, 'stdout': -1, 'text': True}
process = <Popen: returncode: 1 args: ['/usr/local/bin/node', '-e', "\n        global....>
stdout = ''
stderr = '/home/runner/work/The-Nexus-Protocol-Token-DOA/The-Nexus-Protocol-Token-DOA/withdraw.js:101\npragma solidity ^0.8.20;...es/helpers:147:16)\n    at [eval]:10:26\n    at runScriptInThisContext (node:internal/vm:209:10)\n\nNode.js v22.22.3\n'
retcode = 1

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.
    
        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.
    
        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.
    
        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.
    
        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.
    
        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.
    
        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE
    
        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE
    
        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        global.document = {\n          getElementById: () => ({ value: '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac' })\n        };\n        global.ethers = {\n          utils: {\n            isAddress: (value) => /^0x[a-fA-F0-9]{40}$/.test(value)\n          }\n        };\n        const withdraw = require('./withdraw.js');\n        const valid = withdraw.getSettlementDestination();\n        global.document = {\n          getElementById: () => ({ value: '   ' })\n        };\n        const blank = withdraw.getSettlementDestination();\n        global.document = {\n          getElementById: () => ({ value: 'not-an-address' })\n        };\n        const invalid = withdraw.getSettlementDestination();\n        console.log(JSON.stringify({ valid, blank, invalid }));\n        "]' returned non-zero exit status 1.

/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/subprocess.py:571: CalledProcessError
=========================== short test summary info ============================
FAILED nexus/test_withdraw_dashboard.py::test_withdraw_js_runtime_labels_transaction_direction - subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const wallet = '0xeCE999c86452c573Adfdd7F0C9226e673477973a';\n        const parsed = withdraw.parseImportedPayload(JSON.stringify({\n          wallet_address: wallet,\n          transactions: [\n            {\n              chain: 'ethereum',\n              transaction_type: 'Sent USDT',\n              from: wallet,\n              to: '0x1111111111111111111111111111111111111111',\n              amount: '1000000',\n              decimals: 6,\n              symbol: 'USDT'\n            },\n            {\n              chain: 'ethereum',\n              transaction_type: 'Received USDT',\n              from: '0x1111111111111111111111111111111111111111',\n              to: wallet,\n              amount: '2000000',\n              decimals: 6,\n              symbol: 'USDT'\n            }\n          ]\n        }));\n        console.log(JSON.stringify(parsed.transactions.map(tx => ({\n          direction: tx.direction,\n          directionLabel: tx.directionLabel,\n          recipientStatus: tx.recipientStatus,\n          recipientLabel: tx.recipientLabel,\n          recipientWarning: tx.recipientWarning,\n          amountLabel: tx.amountLabel\n        }))));\n        "]' returned non-zero exit status 1.
FAILED nexus/test_withdraw_dashboard.py::test_withdraw_js_runtime_helpers_cover_formatting_and_parsing - subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const validPayload = withdraw.parseImportedPayload(JSON.stringify({\n          wallet_address: '0xabc',\n          balances: [{\n            chain: 'ethereum',\n            address: 'native',\n            amount: '1500000000000000000',\n            symbol: 'ETH',\n            decimals: 18,\n            value_usd: 3200\n          }]\n        }));\n        const invalidJson = (() => {\n          try { withdraw.parseImportedPayload('{'); } catch (error) { return error.message; }\n        })();\n        const nonObject = (() => {\n          try { withdraw.parseImportedPayload('[]'); } catch (error) { return error.message; }\n        })();\n        const emptyPayload = (() => {\n          try {\n            withdraw.parseImportedPayload(JSON.stringify({ balances: [], transactions: [] }));\n          } catch (error) {\n            return error.message;\n          }\n        })();\n        console.log(JSON.stringify({\n          large: withdraw.formatTokenAmount('1000000000000', 6),\n          medium: withdraw.formatTokenAmount('1500000', 6),\n          small: withdraw.formatTokenAmount('12345', 8),\n          wallet: validPayload.walletAddress,\n          balances: validPayload.balances.length,\n          invalidJson,\n          nonObject,\n          emptyPayload\n        }));\n        "]' returned non-zero exit status 1.
FAILED nexus/test_withdraw_dashboard.py::test_withdraw_js_runtime_builds_imported_balance_transfer_requests - subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const readyBalance = {\n          assetType: 'balance',\n          chain: 'base',\n          chainId: 8453,\n          address: '0x1234',\n          rawAmount: '2500000',\n          offRamp: {\n            status: 'ready',\n            settlement: {\n              network: 'Base',\n              supportsDirectTransfer: true\n            }\n          }\n        };\n        const nativeBalance = {\n          assetType: 'balance',\n          chain: 'ethereum',\n          chainId: 1,\n          address: 'native',\n          rawAmount: '1000000000000000000',\n          offRamp: {\n            status: 'ready',\n            settlement: {\n              network: 'Ethereum',\n              supportsDirectTransfer: true\n            }\n          }\n        };\n        const reviewBalance = {\n          assetType: 'balance',\n          chain: 'base',\n          chainId: 8453,\n          address: '0x9999',\n          rawAmount: '1',\n          offRamp: {\n            status: 'review',\n            settlement: {\n              network: 'Base',\n              supportsDirectTransfer: true\n            }\n          }\n        };\n        const tokenRequest = withdraw.buildImportedBalanceTransferRequest(\n          readyBalance,\n          '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac'\n        );\n        const nativeRequest = withdraw.buildImportedBalanceTransferRequest(\n          nativeBalance,\n          '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac'\n        );\n        const invalidStatus = withdraw.validateImportedBalanceTransfer(\n          reviewBalance,\n          '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac',\n          8453\n        );\n        const wrongChain = withdraw.validateImportedBalanceTransfer(\n          readyBalance,\n          '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac',\n          1\n        );\n        console.log(JSON.stringify({\n          canSendReady: withdraw.canSendImportedBalance(readyBalance),\n          canSendReview: withdraw.canSendImportedBalance(reviewBalance),\n          tokenRequest,\n          nativeRequest,\n          invalidStatus,\n          wrongChain\n        }));\n        "]' returned non-zero exit status 1.
FAILED nexus/test_withdraw_dashboard.py::test_withdraw_js_runtime_can_normalize_dune_collectibles_payload - subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        const withdraw = require('./withdraw.js');\n        const imported = withdraw.parseImportedPayload(JSON.stringify({\n          address: '0xd8da6bf26964af9d7eed9e03e53415d37aa96045',\n          entries: [{\n            contract_address: '0x1234',\n            token_standard: 'ERC721',\n            token_id: '1',\n            chain: 'base',\n            chain_id: 8453,\n            name: 'Base Genesis',\n            symbol: 'BG',\n            balance: '1',\n            is_spam: false,\n            last_acquired: '2026-04-06T18:15:47+00:00'\n          }, {\n            contract_address: '0xabcd',\n            token_standard: 'ERC1155',\n            token_id: '9',\n            chain: 'ethereum',\n            chain_id: 1,\n            name: 'Spam Drop',\n            symbol: 'DROP',\n            balance: '2',\n            is_spam: true\n          }]\n        }));\n        console.log(JSON.stringify({\n          wallet: imported.walletAddress,\n          source: imported.source,\n          balances: imported.balances.length,\n          collectibles: imported.collectibles.length,\n          baseNetwork: imported.collectibles[0].offRamp.settlement.network,\n          baseDestination: imported.collectibles[0].offRamp.settlement.destination,\n          spamStatus: imported.collectibles[1].offRamp.status\n        }));\n        "]' returned non-zero exit status 1.
FAILED nexus/test_withdraw_dashboard.py::test_withdraw_js_runtime_settlement_destination_validation - subprocess.CalledProcessError: Command '['/usr/local/bin/node', '-e', "\n        global.document = {\n          getElementById: () => ({ value: '0x1EF9950fc2d9433Ab9d253881fd461f8e2098Eac' })\n        };\n        global.ethers = {\n          utils: {\n            isAddress: (value) => /^0x[a-fA-F0-9]{40}$/.test(value)\n          }\n        };\n        const withdraw = require('./withdraw.js');\n        const valid = withdraw.getSettlementDestination();\n        global.document = {\n          getElementById: () => ({ value: '   ' })\n        };\n        const blank = withdraw.getSettlementDestination();\n        global.document = {\n          getElementById: () => ({ value: 'not-an-address' })\n        };\n        const invalid = withdraw.getSettlementDestination();\n        console.log(JSON.stringify({ valid, blank, invalid }));\n        "]
