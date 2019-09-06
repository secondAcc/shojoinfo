
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
    public class howhard:TabControl
    {
        public howhard()
        {
        }

        private void InitializeComponent()
        {
            this.SuspendLayout();
            this.ResumeLayout(false);

        }
    }
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
                howhard hardtab = new howhard();
                tab.Controls.Add(hardtab);
                hardtab.Location = new Point(1, 1);
                hardtab.Size = new System.Drawing.Size(443, 564);
                this.commonfightTabControl.Controls.Add(tab);
            }
            Console.Write("make check");
        }
    }
}
