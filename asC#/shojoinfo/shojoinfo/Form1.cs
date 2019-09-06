
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
            makecommonfightTabs();
        }
        
        private void makecommonfightTabs()
        {
            for (int i = 0; i < 12; i++)
            {
                string name = i.ToString();
                TabPage tab = new TabPage(i.ToString());
                this.commonfightTabControl.Controls.Add(tab);
            }
            Console.Write("make check");
        }
    }
}
