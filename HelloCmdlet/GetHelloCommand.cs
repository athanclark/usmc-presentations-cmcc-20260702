using System.Management.Automation;

namespace HelloCmdlet {
  [Cmdlet(VerbsCommon.Get, "Hello")]
  public class GetHelloCommand : Cmdlet
  {
    protected override void ProcessRecord()
    {
      WriteObject(new HelloInfo
      {
        Message = "Hello from PowerShell on Linux",
        Platform = System.Runtime.InteropServices.RuntimeInformation.OSDescription
      });
    }
  }

  public class HelloInfo
  {
    public string Message { get; set; } = "";
    public string Platform { get; set; } = "";
  }
}

