
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace shojoinfo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            main();
        }
        public void main()
        {

        }
        private void makeTabs()
        {
            for (int i = 0; i < 4; i++)
            {
                TabPage tab = new TabPage("hello");
                this.tabControl1.Controls.Add(tab);
            }
            Console.Write("make check");
        }
    }
}
